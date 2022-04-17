import ply.yacc as yacc
from lexer import tokens
import sys


# PROGRAMA
def p_program(p):
    '''program : PROGRAM ID SEMI p1 p2 p3 main'''

def p_p1(p):
    '''p1 : class
          | empty'''

def p_p2(p):
    '''p2 : vars
          | empty'''

def p_p3(p):
    '''p3 : function
          | empty'''

def p_class(p):
    '''class : CLASS ID c1 SEMI LB c2 c3 RB SEMI c4'''

def p_c1(p):
    '''c1 : INHERITS ID
          | empty'''

def p_c2(p):
    '''c2 : ATTRIBUTES vars
          | empty'''

def p_c3(p):
    '''c3 : METHODS function
          | empty'''

def p_c4(p):
    '''c4 : class
          | empty'''

def p_vars(p):
    '''vars : VARIABLES v1'''


def p_v1(p):
    '''v1 : lista_ids COLON v2 SEMI v3'''

def p_v2(p):
    '''v2 : ID
          | tipo'''

def p_v3(p):
    '''v3 : v1
          | empty'''

def p_lista_ids(p):
    '''lista_ids: ID l1 l3'''

def p_l1(p):
    '''l1 : LS CTEI l2 RS
          | empty'''

def p_l2(p):
    '''l2 : COMMA CTEI
          | empty'''

def p_l3(p):
    '''l3 : COMMA lista_ids
          | empty'''

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHAR
            | ID'''

def p_function(p):
    '''function : tipo_retorno FUNCTION ID LP params RP SEMI vars LB m1 function_return RB'''

def p_tipo_retorno(p):
    '''tipo_retorno : INT
                    | FLOAT
                    | CHAR
                    | VOID'''

def p_params(p):
    '''params : ID COLON tipo pr1'''

def p_pr1(p):
    '''pr1 : COMMA params
           | empty'''

def p_main(p):
    '''main : MAIN LP RP LB m1 RB'''

def p_m1(p):
    '''m1 : statement m2'''

def p_m2(p):
    '''m2 : m1
          | empty'''

def p_statement(p):
    '''statement : assignment
                 | read
                 | write
                 | if
                 | while
                 | from
                 | void_call
                 | expression'''

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
    yacc.parse(file)
    print(sys.argv[1], "is a valid program.")

if __name__ == '__main__':
    main()

