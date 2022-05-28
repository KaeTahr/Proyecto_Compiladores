from typing import Type
import tablaConst
from cuboSemantico import *
from memoria import *
from dirFunciones import FuncAttr

m_operand_stack = []
operand_stack = []
operator_stack = []
type_stack = []
instruction_pointer = 1
temporal_counter = 1  # total
local_temporal_counter = 1
quad_list = []  # quadruplos con IDs
jump_list = []
from_tmp = []
m_from_tmp = []
m_quad_list = []  # quadruplos con direcciones
m_prefix = ''


def get_instruction_pointer():
    return instruction_pointer


def gen_goto_main():
    global instruction_pointer
    quad_list[0][-1] = instruction_pointer + 1
    m_quad_list[0][-1] = instruction_pointer + 1
    instruction_pointer += 1


# EXPRESSIONS
def gen_quad_exp(valid_operators):
    global operand_stack, operator_stack, type_stack, quad_list, temporal_counter, instruction_pointer, local_temporal_counter
    if operator_stack:
        current_operator = operator_stack[-1]
        if current_operator in valid_operators:
            right_operand = operand_stack.pop()
            right_type = type_stack.pop()
            left_operand = operand_stack.pop()
            left_type = type_stack.pop()
            operator = operator_stack.pop()
            result_type = validateOperation(left_type, right_type, operator)
            if result_type != 'ERROR':
                # IDs
                temp_result = "t" + str(temporal_counter)
                new_quad = [operator, left_operand, right_operand, temp_result]
                quad_list.append(new_quad)
                type_stack.append(result_type)
                operand_stack.append(temp_result)
                # ADDRESSES
                m_temp = get_avail('temporal', result_type)
                m_op = tablaConst.get_oper_code(operator)
                m_right = m_operand_stack.pop()
                m_left = m_operand_stack.pop()
                m_quad = [m_op, m_left, m_right, m_temp]
                m_quad_list.append(m_quad)
                m_operand_stack.append(m_temp)

                instruction_pointer += 1
                temporal_counter += 1
                local_temporal_counter += 1

            else:
                print("ERROR: Type mismatch in expression!")
                exit()


# ASSIGNMENT
def gen_quad_assignment():
    global operand_stack, operator_stack, type_stack, quad_list, temporal_counter, instruction_pointer
    if operator_stack:
        current_operator = operator_stack[-1]
        if current_operator == '=':
            right_operand = operand_stack.pop()
            right_type = type_stack.pop()
            left_operand = operand_stack.pop()
            left_type = type_stack.pop()
            operator = operator_stack.pop()
            result_type = validateOperation(left_type, right_type, operator)
            if result_type != 'ERROR':
                # IDs
                new_quad = [operator, right_operand, '', left_operand]
                quad_list.append(new_quad)
                type_stack.append(result_type)
                # ADDRESS
                m_op = tablaConst.get_oper_code(operator)
                m_right = m_operand_stack.pop()
                m_left = m_operand_stack.pop()
                m_quad = [m_op, m_right, '', m_left]
                m_quad_list.append(m_quad)
                instruction_pointer += 1
            else:
                print("ERROR: Type mismatch in assignment:", left_operand, operator, right_operand)
                exit()


# IF
def gen_quad_if():
    global type_stack, quad_list, instruction_pointer
    exp_type = type_stack.pop()
    if exp_type != 'int':
        print("ERROR Type mismatch!")
        raise TypeError
    else:
        # ID
        result = operand_stack.pop()
        quad_list.append(['GotoF', result, '', 'pending'])
        jump_list.append(instruction_pointer)
        # Memory
        m_res = m_operand_stack.pop()
        m_op = tablaConst.get_oper_code('GOTOF')
        m_quad_list.append([m_op, m_res, '', 'pending'])

        instruction_pointer += 1


def gen_end_if():
    global instruction_pointer
    start = jump_list.pop()
    start -= 1
    quad_list[start][-1] = instruction_pointer
    m_quad_list[start][-1] = instruction_pointer


def gen_quad_else():
    global instruction_pointer, quad_list
    start = jump_list.pop()
    start -= 1
    # ID
    quad_list[start][-1] = instruction_pointer + 1
    result = quad_list[start][1]
    quad_list.append(['GoTo', '', '', 'pending'])
    # Memory
    m_quad_list[start][-1] = instruction_pointer + 1
    m_res = m_quad_list[start][1]
    m_op = tablaConst.get_oper_code('GOTO')
    m_quad_list.append([m_op, '', '', 'pending'])

    jump_list.append(instruction_pointer)
    instruction_pointer += 1


# WHILE
def gen_while_start():
    global instruction_pointer
    jump_list.append(instruction_pointer)


def gen_while_jmp():
    global instruction_pointer
    exp_type = type_stack.pop()
    if exp_type != 'int':
        print("ERROR Type mismatch!")
        raise TypeError
    else:
        result = operand_stack.pop()
        m_res = m_operand_stack.pop()
        m_op = tablaConst.get_oper_code('GOTOF')
        quad_list.append(['GotoF', result, '', 'pending'])
        m_quad_list.append([m_op, m_res, '', 'pending'])
        jump_list.append(instruction_pointer)
        instruction_pointer += 1


def gen_while_end():
    global instruction_pointer
    exit_jmp = jump_list.pop()
    exit_jmp -= 1
    quad_list[exit_jmp][-1] = instruction_pointer + 1
    m_quad_list[exit_jmp][-1] = instruction_pointer + 1
    w_start = jump_list.pop()
    quad_list.append(['GoTo', '', '', w_start])
    m_op = tablaConst.get_oper_code('GOTO')
    m_quad_list.append([m_op, '', '', w_start])
    instruction_pointer += 1


# FROM
def gen_from_start(s, m):
    global instruction_pointer
    exp_type = type_stack.pop()
    if exp_type != 'int':
        print('ERROR Type mismatch!')
        raise TypeError
    from_tmp.append(s)
    from_tmp.append('int')
    m_from_tmp.append(m)  # Memory


def gen_from_jmp():
    global instruction_pointer, temporal_counter, local_temporal_counter
    start_type = from_tmp.pop()
    start = from_tmp.pop()
    m_start = m_from_tmp.pop()  # Memory
    target = operand_stack.pop()
    target_type = type_stack.pop()
    m_target = m_operand_stack.pop()  # Memory

    result_type = validateOperation(start_type, target_type, '<')

    if result_type != 'int':
        print('ERROR Type mismatch!')
        raise TypeError('type was: ' + result_type)

    temp_result = "t" + str(temporal_counter)
    m_temp = get_avail('temporal', result_type)
    temporal_counter += 1
    local_temporal_counter += 1
    quad_list.append(['<', start, target, temp_result])
    m_op = tablaConst.get_oper_code('<')
    m_quad_list.append([m_op, m_start, m_target, m_temp])
    instruction_pointer += 1
    type_stack.append(result_type)
    operand_stack.append(temp_result)
    m_operand_stack.append(m_temp)
    jump_list.append(instruction_pointer)
    quad_list.append(['GoToF', operand_stack.pop(), '', 'pending'])
    m_op = tablaConst.get_oper_code('GOTOF')
    m_quad_list.append([m_op, m_operand_stack.pop(), '', 'pending'])
    instruction_pointer += 1


def gen_from_end():
    global instruction_pointer
    start = jump_list.pop()
    start -= 1
    quad_list[start][-1] = instruction_pointer + 1
    quad_list.append(['GoTo', '', '', start])
    m_quad_list[start][-1] = instruction_pointer + 1
    m_op = tablaConst.get_oper_code('GOTO')
    m_quad_list.append([m_op, '', '', start])
    instruction_pointer += 1


# READ
def gen_quad_read():
    global instruction_pointer, quad_list, operand_stack, type_stack
    # ID
    read_operand = operand_stack.pop()
    read_type = type_stack.pop()
    quad_list.append(['READ', '', '', read_operand])
    # Memory
    m_op = tablaConst.get_oper_code('READ')
    m_operand = m_operand_stack.pop()
    m_quad = [m_op, '', '', m_operand]
    m_quad_list.append(m_quad)
    instruction_pointer += 1


# WRITE
def gen_quad_write():
    global instruction_pointer, quad_list, operand_stack, type_stack
    # ID
    write_operand = operand_stack.pop()
    write_type = type_stack.pop()
    quad_list.append(['WRITE', '', '', write_operand])
    # Memory
    m_op = tablaConst.get_oper_code('WRITE')
    m_operand = m_operand_stack.pop()
    m_quad = [m_op, '', '', m_operand]
    m_quad_list.append(m_quad)
    instruction_pointer += 1


# RETURN
def gen_quad_return(f):
    global instruction_pointer
    curr_type = type_stack.pop()
    res = operand_stack.pop()

    m_res = m_operand_stack.pop()  # Memory
    if f[FuncAttr.IS_GLOBAL] == 'method':
        m_res = res

    if curr_type != f[FuncAttr.RETURN_TYPE]:  # catches void function with return
        print("ERROR: Type mismatch in function return!", f[FuncAttr.RETURN_TYPE], "returns", curr_type)
        exit()
    else:
        quad_list.append(['RETURN', '', '', res])
        quad_list.append(['=', res, '', f[FuncAttr.RETURN_ADDRESS]])
        # Memory
        m_op = tablaConst.get_oper_code('RETURN')
        m_quad_list.append([m_op, '', '', m_res])  # Memory
        m_op = tablaConst.get_oper_code('=')
        m_quad_list.append([m_op, m_res, '', f[FuncAttr.RETURN_ADDRESS]])

        instruction_pointer += 1
        instruction_pointer += 1


# FUNCTIONS
def fun_start():
    global local_temporal_counter
    local_temporal_counter = 1


def fun_end():
    global instruction_pointer, local_temporal_counter
    quad_list.append(['ENDFunc', '', '', ''])
    # Memory
    m_op = tablaConst.get_oper_code('ENDFUNC')
    m_quad_list.append([m_op, '', '', ''])
    instruction_pointer += 1
    return local_temporal_counter


def handle_fun_call(fun_id, df, params_count):
    global instruction_pointer, temporal_counter
    if fun_id not in df:
        raise Exception('Attempted to call undeclared function', fun_id)
    f = df[fun_id]
    signature = (f[FuncAttr.RETURN_TYPE], fun_id, f[FuncAttr.PARAMETERS])
    is_void = signature[0] == 'void'
    # GENERATE ERA
    quad_list.append(['ERA', '', '', fun_id])  # TODO: Is this ok?
    # Memory
    m_op = tablaConst.get_oper_code('ERA')
    m_quad_list.append([m_op, '', '', fun_id])
    instruction_pointer += 1
    # Verify parameters
    # first, verify correct amount
    if len(signature[2]) != params_count:
        raise Exception("Function call doesn't match function signature")
    # now check types
    p_types = []
    for i in range(params_count):
        p_types.append(type_stack.pop())

    p_types.reverse()
    if tuple(p_types) != signature[2]:
        raise TypeError('Mismatch in expected parameters type')
    # Now, initiate parameters with expression result

    m_op = tablaConst.get_oper_code('PARAMETER')
    for i in range(params_count):
        quad_list.append(['PARAMETER', operand_stack.pop(), '', params_count - i])
        m_quad_list.append([m_op, m_operand_stack.pop(), '', params_count - i])
        instruction_pointer += 1

    # OK, try to execute
    quad_list.append(['GoSub', fun_id, '', f[FuncAttr.START]])  # TODO: is fun_id used in run time
    # Memory
    m_op = tablaConst.get_oper_code('GOSUB')
    m_quad_list.append([m_op, fun_id, '', f[FuncAttr.START]])
    instruction_pointer += 1
    if not is_void:  # No es una expresion si es void
        m_temp = get_avail('temporal', f[FuncAttr.RETURN_TYPE])
        temp_result = "t" + str(temporal_counter)
        temporal_counter += 1
        m_op = tablaConst.get_oper_code('=')
        m_quad_list.append([m_op, f[FuncAttr.RETURN_ADDRESS], '', m_temp])
        quad_list.append(['=', f[FuncAttr.RETURN_ADDRESS], '', temp_result])
        instruction_pointer += 1
        type_stack.append(signature[0])
        operand_stack.append(temp_result)
        m_operand_stack.append(m_temp)


def print_id_q():
    print("\nQuadruples:")
    for i, q in enumerate(quad_list):
        print(i + 1, q)


def print_mem_q():
    print("\nQuadruples:")
    for i, q in enumerate(m_quad_list):
        print(i + 1, q)


def print_all_q():
    print("\nQuadruples:")
    for i in range(len(quad_list)):
        print(i + 1, str(quad_list[i]) + "\t " + str(m_quad_list[i]))


def set_prefix(p):
    global m_prefix
    m_prefix = p