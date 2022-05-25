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
temporal_counter = 1 # total
local_temporal_counter = 1
quad_list = []  # quadruplos con IDs
jump_list = []
from_tmp = []
m_quad_list = []  # quadruplos con direcciones

def get_instruction_pointer():
    return instruction_pointer

# gen_quad 0-4
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


# gen_quad 5
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
                instruction_pointer += 1
                type_stack.append(result_type)
                #operand_stack.append(left_operand) # TODO: Se debe regresar resultado a stack de operandos?
                # ADDRESS
                m_op = tablaConst.get_oper_code(operator)
                m_right = m_operand_stack.pop()
                m_left = m_operand_stack.pop()
                m_quad = [m_op, m_right, '', m_left]
                m_quad_list.append(m_quad)
                # .append(m_left)
            else:
                print("ERROR: Type mismatch in assignment!", operator, left_type, right_type)
                exit()


# gen_quad 6
def gen_quad_if():
    global type_stack, quad_list, instruction_pointer
    exp_type = type_stack.pop()
    if exp_type != 'int':
        print("ERROR Type mismatch!")
        raise TypeError
    else:
        result = operand_stack.pop()  # TODO check this
        quad_list.append(['GotoF', result, '', 'pending'])
        jump_list.append(instruction_pointer)
        instruction_pointer += 1


def gen_end_if():
    global instruction_pointer
    start = jump_list.pop()
    start -= 1
    quad_list[start][-1] = instruction_pointer


def gen_quad_else():
    global instruction_pointer, quad_list
    start = jump_list.pop()
    start -= 1
    quad_list[start][-1] = instruction_pointer
    result = quad_list[start][1]
    quad_list.append(['GoToT', result, '', 'pending'])
    jump_list.append(instruction_pointer)
    instruction_pointer += 1


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
        result = operand_stack.pop()  # TODO check this
        quad_list.append(['GotoF', result, '', 'pending'])
        jump_list.append(instruction_pointer)
        instruction_pointer += 1


def gen_while_end():
    global instruction_pointer
    exit_jmp = jump_list.pop()
    exit_jmp -= 1
    quad_list[exit_jmp][-1] = instruction_pointer + 1
    w_start = jump_list.pop()
    quad_list.append(['GoTo', '', '', w_start])
    instruction_pointer += 1


# FROM
def gen_from_start(s):
    global instruction_pointer
    exp_type = type_stack.pop()
    if exp_type != 'int':
        print('ERROR Type mismatch!')
        raise TypeError
    from_tmp.append(s)
    from_tmp.append('int')


def gen_from_jmp():
    global instruction_pointer, temporal_counter, local_temporal_counter
    start_type = from_tmp.pop()
    start = from_tmp.pop()
    target = operand_stack.pop()
    target_type = type_stack.pop()

    result_type = validateOperation(start_type, target_type, '<')
    if result_type != 'int':
        print('ERROR Type mismatch!')
        raise TypeError('type was: ' + result_type)

    temp_result = "t" + str(temporal_counter)
    temporal_counter += 1
    local_temporal_counter += 1
    quad_list.append(['>', start, target, temp_result])
    instruction_pointer += 1
    type_stack.append(result_type)
    operand_stack.append(temp_result)
    jump_list.append(instruction_pointer)
    quad_list.append(['GoToF', operand_stack.pop(), '', 'pending'])
    instruction_pointer += 1


def gen_from_end():
    global instruction_pointer
    start = jump_list.pop()
    start -= 1
    quad_list[start][-1] = instruction_pointer + 1
    quad_list.append(['GoTo', '', '', start])
    instruction_pointer += 1


def gen_quad_read():
    global instruction_pointer, quad_list, operand_stack, type_stack
    read_operand = operand_stack.pop()
    read_type = type_stack.pop()
    quad_list.append(['READ', '', '', read_operand])
    instruction_pointer += 1


def gen_quad_write():
    global instruction_pointer, quad_list, operand_stack, type_stack
    write_operand = operand_stack.pop()
    write_type = type_stack.pop()
    quad_list.append(['WRITE', '', '', write_operand])
    instruction_pointer += 1


#  gen_quad 9
def gen_quad_return(f):
    global instruction_pointer, quad_list, operand_stack, type_stack
    curr_type = type_stack.pop()
    res = operand_stack.pop()
    if curr_type != f[FuncAttr.RETURN_TYPE]:
        print("ERROR: Type mismatch in function return!")
        exit()
    else:
        quad_list.append(['RETURN', '', '', res])
        instruction_pointer += 1
        quad_list.append(['=', res, '', f[FuncAttr.RETURN_ADDRESS]])

def fun_start():
    global local_temporal_counter
    local_temporal_counter = 1

def fun_end():
    global instruction_pointer, local_temporal_counter
    quad_list.append(['ENDFunc', '', '', ''])
    instruction_pointer += 1
    return  local_temporal_counter

def handle_fun_call(fun_id, df, params_count):
    global instruction_pointer
    if fun_id not in df:
        raise Exception('Attempted to call undeclared function', fun_id)
    f = df[fun_id]
    signature = (f[FuncAttr.RETURN_TYPE], fun_id,  f[FuncAttr.PARAMETERS]) 
    is_void = signature[0] == 'void'
    # GENERATE ERA
    quad_list.append(['ERA', '', '', fun_id]) # TODO: Is this ok?
    instruction_pointer += 1
    # Verifiy parameters
    # first, verify correct amount
    if len(signature[2]) != params_count:
        raise Exception("Function call doesn't match function signature")
    # now check types
    # TODO: Are the last operations in the stack the parameters? 
    # should be?
    p_types = []
    for i in range(params_count):
        p_types.append(type_stack.pop())

    p_types.reverse()
    if tuple(p_types) != signature[2]:
        raise TypeError('Mismatch in expected parameters type')
    # Now, initiate parameters with expression result

    #breakpoint()
    for i in range(params_count):
        quad_list.append(('PARAMETER', operand_stack.pop(), '', params_count - i))
    # TODO: Remember where we were called from? Returns managed by VM?
    # OK, try to execute
    quad_list.append(['GoSub', fun_id, '', f[FuncAttr.START]])
    instruction_pointer += 1
    if not is_void: # No es una expresion si es void
        type_stack.append(signature[0])
        operand_stack.append(f[FuncAttr.RETURN_ADDRESS]) # TODO: What is the result of the function as an expression?

   
