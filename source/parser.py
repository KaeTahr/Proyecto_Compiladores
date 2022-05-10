import ply.yacc as yacc
import dirFunciones
import tablaVars
from lexer import tokens
import sys

curr_fun_type = ''
curr_var_type = ''
curr_var_id = ''
curr_scope = ''


# PROGRAMA
def p_program(p):
    '''program : PROGRAM ID store_program SEMI prog1 prog2 prog3 main'''
    tablaVars.print_var_table()
    p[0] = "\nInput is a valid program.\n"


def p_store_program(p):
    "store_program :"
    dirFunciones.add_function(p[-1], p[-2], p[-2])
    global curr_scope
    curr_scope = p[-1]


def p_prog1(p):
    '''prog1 : class
             | empty'''


def p_prog2(p):
    '''prog2 : vars
             | empty'''


def p_prog3(p):
    '''prog3 : function
             | empty'''


# CLASS
def p_class(p):
    '''class : CLASS ID class1 LB class2 class3 RB SEMI class4'''


def p_class1(p):
    '''class1 : INHERITS ID
              | empty'''


def p_class2(p):
    '''class2 : attrs
              | empty'''


def p_class3(p):
    '''class3 : mthds
              | empty'''


def p_class4(p):
    '''class4 : class
              | empty'''


def p_attrs(p):
    '''attrs : ATTRIBUTES attrs1'''


def p_attrs1(p):
    '''attrs1 : tipo COLON lista_ids SEMI attrs2'''


def p_attrs2(p):
    '''attrs2 : attrs1
              | empty'''


def p_mthds(p):
    '''mthds : METHODS function'''


# VARS
def p_vars(p):
    '''vars : VARIABLES LB attrs1 RB'''


def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHAR
            | ID'''
    global curr_var_type
    curr_var_type = p[1]


def p_lista_ids(p):
    '''lista_ids : ID list1 list2'''
    global curr_var_id
    curr_var_id = p[1]
    tablaVars.add_variable(curr_var_id, curr_var_type, "variable", curr_scope)


# def p_store_id(p):
#     '''store_id :'''
#     global curr_var_id



def p_list1(p):
    '''list1 : LS CTEI RS
             | LS CTEI COMMA CTEI RS
             | empty'''


def p_list2(p):
    '''list2 : COMMA lista_ids
             | empty'''


# MAIN
def p_main(p):
    '''main : MAIN LP RP LB main1 RB'''


def p_main1(p):
    '''main1 : statement
             | empty'''


# FUNCTION
def p_function(p):
    '''function : tipo_retorno FUNCTION ID store_function LP func1 RP LB func2 statement RB func3'''


def p_store_function(p):
    "store_function :"
    global curr_fun_type, curr_scope
    dirFunciones.add_function(p[-1], curr_fun_type, p[-2])
    curr_scope = p[-1]


def p_func1(p):
    '''func1 : params
             | empty'''


def p_func2(p):
    '''func2 : vars
             | empty'''


def p_func3(p):
    '''func3 : function
             | empty'''


def p_tipo_param(p):
    '''tipo_param : INT
                  | FLOAT
                  | CHAR'''


def p_params(p):
    '''params : ID COLON tipo_param par1'''


def p_par1(p):
    '''par1 : COMMA params
            | empty'''


def p_tipo_retorno(p):
    '''tipo_retorno : INT
                    | FLOAT
                    | CHAR
                    | VOID'''
    global curr_fun_type
    curr_fun_type = p[1]


# STATEMENT
def p_statement(p):
    '''statement : assignment SEMI stmt1
                 | void_call SEMI stmt1
                 | read SEMI stmt1
                 | write SEMI stmt1
                 | if_st stmt1
                 | while_st stmt1
                 | from_st stmt1
                 | return_st SEMI stmt1'''


def p_stmt1(p):
    '''stmt1 : statement
             | empty'''


# ASSIGNMENT
def p_assignment(p):
    '''assignment : var EQ expression'''


def p_var(p):
    '''var : ID list1
           | ID DOT ID'''


# VOID CALL
def p_void_call(p):
    '''void_call : ID call1 LP call2 RP
                 | ID call1 LP RP'''


def p_call1(p):
    '''call1 : DOT ID
             | empty'''


def p_call2(p):
    '''call2 : expression call3'''


def p_call3(p):
    '''call3 : COMMA call2
             | empty'''


# READ
def p_read(p):
    '''read : READ LP var RP'''


# WRITE
def p_write(p):
    '''write : WRITE LP write1 RP'''


def p_write1(p):
    '''write1 : expression write2
              | CTES write2'''


def p_write2(p):
    '''write2 : COMMA write1
              | empty'''


# IF
def p_if_st(p):
    '''if_st : IF LP expression RP THEN LB statement RB if1'''


def p_if1(p):
    '''if1 : ELSE LB statement RB
           | empty'''


# WHILE
def p_while_st(p):
    '''while_st : WHILE LP expression RP DO LB statement RB'''


# FROM
def p_from_st(p):
    '''from_st : FROM ID EQ expression UNTIL expression DO LB statement RB'''


# RETURN
def p_return_st(p):
    '''return_st : RETURN LP expression RP'''


# EXPRESSION
def p_expression(p):
    '''expression : exp OR exp
                  | exp'''


def p_exp(p):
    '''exp : k_exp AND exp
           | k_exp'''


def p_k_exp(p):
    '''k_exp : m_exp
             | m_exp LT k_exp
             | m_exp GT k_exp
             | m_exp COMP k_exp
             | m_exp NE k_exp
             | m_exp GTE k_exp
             | m_exp LTE k_exp'''


def p_m_exp(p):
    '''m_exp : term
             | term PLUS m_exp
             | term MIN m_exp'''


def p_term(p):
    '''term : fact
            | fact MUL term
            | fact DIV term'''


def p_fact(p):
    '''fact : LP expression RP
            | void_call
            | var_cte
            | var'''


def p_var_cte(p):
    '''var_cte : CTEI
               | CTEF
               | CTEC'''


# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error in input! ", p)
    else:
        print("Syntax error at EOF!")


def p_empty(p):
    '''empty :'''
    pass


def main():
    # Build the parser
    parser = yacc.yacc()
    file = open(sys.argv[1]).read()
    result = yacc.parse(file)
    print(result)


if __name__ == '__main__':
    main()
