from socket import J1939_FILTER_MAX
from cuboSemantico import *
import pdb

operand_stack = []
operator_stack = []
type_stack = []
instruction_pointer = 1
temporal_counter = 1
quad_list = []
jump_list = []


# gen_quad 1-4
def gen_quad_exp(valid_operators):
    global operand_stack, operator_stack, type_stack, quad_list, temporal_counter, instruction_pointer
    if operator_stack:
        current_operator = operator_stack[-1]
        if current_operator in valid_operators:
            right_operand = operand_stack.pop()
            right_type = type_stack.pop()
            left_operand = operand_stack.pop()
            left_type = type_stack.pop()
            operator = operator_stack.pop()
            result_type = validateOperation(left_type, right_type, operator)
            if result_type != "ERROR":
                temp_result = "t" + str(temporal_counter)
                new_quad = [operator, left_operand, right_operand, temp_result]
                quad_list.append(new_quad)
                instruction_pointer += 1
                temporal_counter += 1
                type_stack.append(result_type)
                operand_stack.append(temp_result)
            else:
                print("ERROR: Type mismatch!")
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
            if result_type != "ERROR":
                new_quad = [operator, right_operand, '', left_operand]
                quad_list.append(new_quad)
                instruction_pointer += 1
                type_stack.append(result_type)
                operand_stack.append(left_operand)
            else:
                print("ERROR: Type mismatch!")
                raise TypeError

def gen_quad_if():
    global type_stack, quad_list, instruction_pointer
    exp_type = type_stack.pop()
    if (exp_type != 'int'):
        print("ERROR Type mismatch!")
        raise TypeError
    else:
        result = operand_stack.pop() #TODO check this
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
    instruction_pointer +=1


def gen_while_start():
    global instruction_pointer
    jump_list.append(instruction_pointer)

def gen_while_jmp():
    global instruction_pointer
    exp_type = type_stack.pop()
    if (exp_type != 'int'):
        print("ERROR Type mismatch!")
        raise TypeError
    else:
        result = operand_stack.pop() #TODO check this
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

