from cuboSemantico import *

operand_stack = []
operator_stack = []
type_stack = []
instruction_pointer = 1
temporal_counter = 1
quad_list = []


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
                exit()
