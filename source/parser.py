import ply.yacc as yacc
import dirFunciones
import tablaVars
from quadruples import *
from lexer import tokens
import sys

curr_fun_type = ''
curr_var_type = ''
curr_var_id = ''
curr_scope = ''
curr_operand_type = ''


# PROGRAMA
def p_program(p):
    """program : PROGRAM ID store_program SEMI prog1 prog2 prog3 main"""
    tablaVars.print_var_table()
    # print("\nOperand stack:\t", operand_stack)
    # print("Type stack:\t", type_stack)
    # print("Operator stack:\t", operator_stack)
    print("Quadruples:\n", *quad_list, sep="\n")
    p[0] = "\nInput is a valid program.\n"


def p_store_program(p):
    """store_program :"""
    dirFunciones.add_function(p[-1], p[-2], p[-2])
    global curr_scope
    curr_scope = p[-1]


def p_prog1(p):
    """prog1 : class
             | empty"""


def p_prog2(p):
    """prog2 : vars
             | empty"""


def p_prog3(p):
    """prog3 : function
             | empty"""


# CLASS
def p_class(p):
    """class : CLASS ID class1 LB class2 class3 RB SEMI class4"""


def p_class1(p):
    """class1 : INHERITS ID
              | empty"""


def p_class2(p):
    """class2 : attrs
              | empty"""


def p_class3(p):
    """class3 : mthds
              | empty"""


def p_class4(p):
    """class4 : class
              | empty"""


def p_attrs(p):
    """attrs : ATTRIBUTES attrs1"""


def p_attrs1(p):
    """attrs1 : tipo COLON lista_ids SEMI attrs2"""


def p_attrs2(p):
    """attrs2 : attrs1
              | empty"""


def p_mthds(p):
    """mthds : METHODS function"""


# VARS
def p_vars(p):
    """vars : VARIABLES LB attrs1 RB"""


def p_tipo(p):
    """tipo : INT
            | FLOAT
            | CHAR
            | ID"""
    global curr_var_type
    curr_var_type = p[1]


def p_lista_ids(p):
    """lista_ids : ID list1 list2"""
    global curr_var_id
    curr_var_id = p[1]
    tablaVars.add_variable(curr_var_id, curr_var_type, "variable", curr_scope)  # save local variable in current scope


def p_list1(p):
    """list1 : LS CTEI RS
             | LS CTEI COMMA CTEI RS
             | empty"""


def p_list2(p):
    """list2 : COMMA lista_ids
             | empty"""


# MAIN
def p_main(p):
    """main : MAIN LP RP LB main1 RB"""


def p_main1(p):
    """main1 : statement
             | empty"""


# FUNCTION
def p_function(p):
    """function : tipo_retorno FUNCTION ID store_function LP func1 RP LB func2 statement RB func3"""


def p_store_function(p):
    """store_function :"""
    global curr_fun_type, curr_scope
    dirFunciones.add_function(p[-1], curr_fun_type, p[-2])  # add function to directory
    curr_scope = p[-1]  # update current scope


def p_func1(p):
    """func1 : params
             | empty"""


def p_func2(p):
    """func2 : vars
             | empty"""


def p_func3(p):
    """func3 : function
             | empty"""


def p_tipo_param(p):
    """tipo_param : INT
                  | FLOAT
                  | CHAR"""
    global curr_var_type
    curr_var_type = p[1]  # save variable/parameter type


def p_params(p):
    """params : ID COLON tipo_param par1"""
    global curr_var_id
    curr_var_id = p[1]
    tablaVars.add_variable(curr_var_id, curr_var_type, "parameter", curr_scope)  # save parameter as local variable


def p_par1(p):
    """par1 : COMMA params
            | empty"""


def p_tipo_retorno(p):
    """tipo_retorno : INT
                    | FLOAT
                    | CHAR
                    | VOID"""
    global curr_fun_type
    curr_fun_type = p[1]  # save function type


# STATEMENT
def p_statement(p):
    """statement : assignment SEMI stmt1
                 | void_call SEMI stmt1
                 | read SEMI stmt1
                 | write SEMI stmt1
                 | if_st stmt1
                 | while_st stmt1
                 | from_st stmt1
                 | return_st SEMI stmt1"""


def p_stmt1(p):
    """stmt1 : statement
             | empty"""


# ASSIGNMENT
def p_assignment(p):
    """assignment : var EQ store_operator expression gen_quad5"""


def p_gen_quad5(p):
    """gen_quad5 :"""
    gen_quad_assignment()


def p_var(p):
    """var : ID store_operand list1
           | ID DOT ID"""


def p_store_operand(p):
    """store_operand :"""
    global curr_operand_type
    operand_stack.append(p[-1])
    curr_operand_type = dirFunciones.get_var_type(p[-1], curr_scope)
    type_stack.append(curr_operand_type)


# VOID CALL
def p_void_call(p):
    """void_call : ID call1 LP call2 RP
                 | ID call1 LP RP"""


def p_call1(p):
    """call1 : DOT ID
             | empty"""


def p_call2(p):
    """call2 : expression call3"""


def p_call3(p):
    """call3 : COMMA call2
             | empty"""


# READ
def p_read(p):
    """read : READ LP var RP"""


# WRITE
def p_write(p):
    """write : WRITE LP write1 RP"""


def p_write1(p):
    """write1 : expression write2
              | CTES write2"""


def p_write2(p):
    """write2 : COMMA write1
              | empty"""


# IF
def p_if_st(p):
    """if_st : IF LP expression RP THEN LB statement RB if1"""


def p_if1(p):
    """if1 : ELSE LB statement RB
           | empty"""


# WHILE
def p_while_st(p):
    """while_st : WHILE LP expression RP DO LB statement RB"""


# FROM
def p_from_st(p):
    """from_st : FROM ID EQ expression UNTIL expression DO LB statement RB"""


# RETURN
def p_return_st(p):
    """return_st : RETURN LP expression RP"""


# EXPRESSION
def p_expression(p):
    """expression : exp gen_quad4 OR store_operator expression
                  | exp gen_quad4"""


def p_gen_quad4(p):
    """gen_quad4 :"""
    valid_operators = ['||']
    gen_quad_exp(valid_operators)


def p_exp(p):
    """exp : k_exp gen_quad3 AND store_operator exp
           | k_exp gen_quad3"""


def p_gen_quad3(p):
    """gen_quad3 :"""
    valid_operators = ['&']
    gen_quad_exp(valid_operators)


def p_k_exp(p):
    """k_exp : m_exp gen_quad2
             | m_exp gen_quad2 LT store_operator k_exp
             | m_exp gen_quad2 GT store_operator k_exp
             | m_exp gen_quad2 COMP store_operator k_exp
             | m_exp gen_quad2 NE store_operator k_exp
             | m_exp gen_quad2 GTE store_operator k_exp
             | m_exp gen_quad2 LTE store_operator k_exp"""


def p_gen_quad2(p):
    """gen_quad2 :"""
    valid_operators = ['<', '>', '==', '!=', '>=', '<=']
    gen_quad_exp(valid_operators)


def p_m_exp(p):
    """m_exp : term gen_quad1
             | term gen_quad1 PLUS store_operator m_exp
             | term gen_quad1 MIN store_operator m_exp"""


def p_gen_quad1(p):
    """gen_quad1 :"""
    valid_operators = ['+', '-']
    gen_quad_exp(valid_operators)


def p_term(p):
    """term : fact gen_quad0
            | fact gen_quad0 MUL store_operator term
            | fact gen_quad0 DIV store_operator term"""


def p_gen_quad0(p):
    """gen_quad0 :"""
    valid_operators = ['*', '/']
    gen_quad_exp(valid_operators)


def p_store_operator(p):
    """store_operator :"""
    operator_stack.append(p[-1])


def p_fact(p):
    """fact : LP store_operator expression RP paren_end
            | void_call
            | var_cte
            | var"""


def p_paren_end(p):
    """paren_end :"""
    current_operator = operator_stack[-1]
    if current_operator == '(':
        operator_stack.pop()


def p_var_cte(p):
    """var_cte : CTEI store_int
               | CTEF store_float
               | CTEC store_char"""


def p_store_int(p):
    """store_int :"""
    operand_stack.append(p[-1])
    type_stack.append('int')


def p_store_float(p):
    """store_float :"""
    operand_stack.append(p[-1])
    type_stack.append('float')


def p_store_char(p):
    """store_char :"""
    operand_stack.append(p[-1])
    type_stack.append('char')


# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error in input! ", p)
        exit()
    else:
        print("Syntax error at EOF!")


def p_empty(p):
    """empty :"""
    pass


def main():
    # Build the parser
    parser = yacc.yacc()
    file = open(sys.argv[1]).read()
    result = yacc.parse(file)
    print(result)


if __name__ == '__main__':
    main()
