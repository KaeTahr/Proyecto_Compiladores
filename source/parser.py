import ply.yacc as yacc
import dirFunciones
from lexer import tokens
import sys

curr_fun_type = ''

# PROGRAMA
def p_program(p):
    '''program : PROGRAM ID store_program SEMI prog1 prog2 prog3 main'''
    p[0] = "Input is a valid program.\n"

def p_store_program(p):
    "store_program :"
    dirFunciones.addFunction(p[-1], p[-2], p[-2])

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
    '''class : class class
             | CLASS ID class1 LB class2 class3 RB SEMI'''


def p_class1(p):
    '''class1 : INHERITS ID
              | empty'''


def p_class2(p):
    '''class2 : attrs
              | empty'''


def p_class3(p):
    '''class3 : mthds
              | empty'''


def p_attrs(p):
    '''attrs : ATTRIBUTES attrs1'''


def p_attrs1(p):
    '''attrs1 : lista_ids COLON tipo SEMI attrs2'''


def p_attrs2(p):
    '''attrs2 : attrs1
              | empty'''


def p_mthds(p):
    '''mthds : METHODS function'''


# VARS
def p_vars(p):
    '''vars : VARIABLES attrs1'''


def p_tipo(p):
    '''tipo : tipo_param
            | ID'''


def p_lista_ids(p):
    '''lista_ids : ID list1 list2'''


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
    '''function : function function
                | tipo_retorno FUNCTION ID store_function LP func1 RP LB func2 main1 RB'''


def p_store_function(p):
    "store_function :"
    global curr_fun_type
    dirFunciones.addFunction(p[-1], curr_fun_type, p[-2])


def p_func1(p):
    '''func1 : params
             | empty'''


def p_func2(p):
    '''func2 : vars
             | empty'''


def p_tipo_param(p):
    '''tipo_param : INT
                  | FLOAT
                  | CHAR'''
    global curr_fun_type

    curr_fun_type = p[1]


def p_params(p):
    '''params : ID COLON tipo_param par1'''


def p_par1(p):
    '''par1 : COMMA params
            | empty'''


def p_tipo_retorno(p):
    '''tipo_retorno : tipo_param
                    | VOID'''
    global curr_fun_type

    if p[1] == "void":
        curr_fun_type = "void"



# STATEMENT
def p_statement(p):
    '''statement : statement statement
                 | assignment SEMI
                 | void_call SEMI
                 | read SEMI
                 | write SEMI
                 | if_st
                 | while_st
                 | from_st
                 | return_st SEMI'''


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
    '''call2 : expression
             | call2 COMMA call2'''
# READ
def p_read(p):
    '''read : READ LP var read1 RP'''


def p_read1(p):
    '''read1 : COMMA var
             | empty'''


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
    '''if1 : ELSE LB main1 RB
           | empty'''


# WHILE
def p_while_st(p):
    '''while_st : WHILE LP expression RP DO LB main1 RB'''


# FROM
def p_from_st(p):
    '''from_st : FROM ID list1 EQ expression UNTIL expression DO LB main1 RB'''


# RETURN
def p_return_st(p):
    '''return_st : RETURN LP expression RP'''


# EXPRESSION
def p_expression(p):
    '''expression : exp
                  | exp OR exp'''


def p_exp(p):
    '''exp : k_exp
           | k_exp AND k_exp'''


def p_k_exp(p):
    '''k_exp : m_exp
             | m_exp LT m_exp
             | m_exp GT m_exp
             | m_exp COMP m_exp
             | m_exp NE m_exp
             | m_exp LTE m_exp
             | m_exp GTE m_exp'''


def p_m_exp(p):
    '''m_exp : term
             | term PLUS term
             | term MIN term'''


def p_term(p):
    '''term : fact
            | fact MUL fact
            | fact DIV fact'''


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
