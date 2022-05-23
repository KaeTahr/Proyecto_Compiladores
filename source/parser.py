import ply.yacc as yacc
import dirFunciones
import tablaVars
import tablaConst
from quadruples import *
from tablaObjetos import *
from lexer import tokens
import sys

curr_fun_type = ''
curr_var_type = ''
curr_var_id = ''
curr_scope = ''
curr_operand_type = ''
curr_from_var = ''
scope_global = ''
in_object = False
curr_class = ''


# PROGRAMA
def p_program(p):
    """program : PROGRAM ID store_program SEMI prog1 prog2 prog3 main"""
    tablaVars.print_var_table()
    # print_obj_table()
    # tablaConst.print_const_table()
    # print("\nOperand stack:\t", operand_stack)
    # print("Type stack:\t", type_stack)
    # print("Operator stack:\t", operator_stack)
    # print("\nQuadruples:")
    # for i, q in enumerate(quad_list):
    #     print(i + 1, q)
    # print("M_Quads:", *m_quad_list, sep="\n")
    p[0] = "\nInput is a valid program.\n"


def p_store_program(p):
    """store_program :"""
    dirFunciones.add_function(p[-1], p[-2], p[-2])
    global curr_scope, scope_global
    curr_scope = p[-1]
    scope_global = p[-1]


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
    """class : CLASS ID store_object class1 LB class2 class3 RB SEMI exit_class class4"""


def p_store_object(p):
    """store_object :"""
    global in_object, curr_class
    curr_class = p[-1]
    add_object(p[-1])  # add object to object table
    in_object = True  # now inside class definition


def p_exit_class(p):
    """exit_class :"""
    global curr_scope, in_object
    curr_scope = scope_global  # return to global scope after class definitions
    in_object = False


def p_class1(p):
    """class1 : INHERITS ID validate_inheritance
              | empty"""


def p_validate_inheritance(p):
    """validate_inheritance :"""
    global curr_class
    validate_class(p[-1])  # make sure parent class is defined
    curr_class = p[-4]
    assign_parent(curr_class, p[-1])


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
    """lista_ids : ID store_id list1 list2"""


def p_store_id(p):
    """store_id :"""
    global curr_var_id
    curr_var_id = p[-1]
    if in_object:  # id read is an attribute within a class
        add_attribute(curr_class, curr_var_id, curr_var_type)
    else:
        if curr_var_type not in ['int', 'float', 'char']:
            tablaVars.add_variable(curr_var_id, curr_var_type, "object", curr_scope)
            tablaVars.instantiate_obj(curr_var_id, curr_var_type, curr_scope)
        else:
            tablaVars.add_variable(curr_var_id, curr_var_type, "variable", curr_scope)


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
    global curr_scope
    if in_object:  # id read is a method within a class
        add_method(curr_class, p[-1], curr_fun_type)
        dirFunciones.add_function(p[-1], curr_fun_type, "method")
    else:
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
    """params : ID COLON tipo_param store_param par1"""


def p_store_param(p):
    """store_param :"""
    tablaVars.add_variable(p[-3], curr_var_type, "parameter", curr_scope)  # save parameter as local variable


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
    p[0] = p[1]


def p_gen_quad5(p):
    """gen_quad5 :"""
    gen_quad_assignment()


def p_var(p):
    """var : ID store_operand list1
           | ID DOT ID store_attr"""


def p_store_attr(p):
    """store_attr :"""
    global curr_operand_type
    name = str(p[-3] + p[-2] + p[-1])
    operand_stack.append(name)
    m_operand_stack.append(dirFunciones.get_var_address(name))
    
    curr_operand_type = dirFunciones.get_var_type(name, curr_scope, curr_class)
    type_stack.append(curr_operand_type)


def p_store_operand(p):
    """store_operand :"""
    global curr_operand_type
    operand_stack.append(p[-1])
    m_operand_stack.append(dirFunciones.get_var_address(p[-1]))
    curr_operand_type = dirFunciones.get_var_type(p[-1], curr_scope, curr_class)
    type_stack.append(curr_operand_type)


# VOID CALL
def p_void_call(p):
    """void_call : ID call1 LP call2 RP
                 | ID call1 LP RP"""


def p_call1(p):
    """call1 : DOT ID found_method
             | empty"""


def p_found_method(p):
    """found_method :"""
    obj = dirFunciones.get_var_type(p[-3], curr_scope, curr_class)
    validate_method(obj, p[-1])


def p_call2(p):
    """call2 : expression call3"""


def p_call3(p):
    """call3 : COMMA call2
             | empty"""


# READ
def p_read(p):
    """read : READ LP var RP"""
    gen_quad_read()


# WRITE
def p_write(p):
    """write : WRITE LP write1 RP"""


def p_write1(p):
    """write1 : expression gen_quad_8 write2
              | CTES store_string gen_quad_8 write2"""


def p_store_string(p):
    """store_string :"""
    type_stack.append('STRING')
    operand_stack.append(p[-1])


def p_gen_quad_8(p):
    """gen_quad_8 :"""
    gen_quad_write()


def p_write2(p):
    """write2 : COMMA write1
              | empty"""


# IF
def p_if_st(p):
    """if_st : IF LP expression RP gen_quad_6 THEN  LB statement RB if1"""


def p_gen_quad_6(p):
    """gen_quad_6 : """
    gen_quad_if()


def p_if1(p):
    """if1 : ELSE LB gen_quad_else statement RB gen_quad_fi
           | gen_quad_fi """


def p_gen_quad_fi(p):
    """gen_quad_fi : """
    gen_end_if()


def p_gen_quad_else(p):
    """gen_quad_else : """
    gen_quad_else()


# WHILE
def p_while_st(p):
    """while_st : WHILE LP gen_while_start expression gen_while_jmp RP DO LB statement RB gen_while_end"""


def p_while_start(p):
    """gen_while_start : """
    gen_while_start()


def p_while_jmp(p):
    """gen_while_jmp : """
    gen_while_jmp()


def p_while_end(p):
    """gen_while_end : """
    gen_while_end()


# FROM
def p_from_st(p):
    """from_st : FROM assignment gen_from_start UNTIL expression gen_from_jmp DO LB statement RB gen_from_end"""
    global curr_from_var
    curr_from_var = p[2]


def p_gen_from_start(p):
    """gen_from_start : """
    global curr_from_var
    gen_from_start(curr_from_var)


def p_gen_from_jmp(p):
    """gen_from_jmp : """
    gen_from_jmp()


def p_gen_from_end(p):
    """gen_from_end : """
    gen_from_end()


# RETURN
def p_return_st(p):
    """return_st : RETURN LP expression gen_quad_9 RP"""


def p_gen_quad_9(p):
    """gen_quad_9 :"""
    gen_quad_return(curr_fun_type)


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
    tablaConst.add_constant(p[-1], 'int')
    m_operand_stack.append(tablaConst.get_const_add(p[-1]))


def p_store_float(p):
    """store_float :"""
    operand_stack.append(p[-1])
    type_stack.append('float')
    tablaConst.add_constant(p[-1], 'float')
    m_operand_stack.append(tablaConst.get_const_add(p[-1]))


def p_store_char(p):
    """store_char :"""
    operand_stack.append(p[-1])
    type_stack.append('char')
    tablaConst.add_constant(p[-1], 'char')
    m_operand_stack.append(tablaConst.get_const_add(p[-1]))


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
