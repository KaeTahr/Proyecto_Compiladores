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

def p_assignment(p):
    '''assignment : var_id EQ expression SEMI'''

def p_var_id(p):
    '''var_id : simple_id var_id1'''

def p_var_id1(p):
    '''var_id1 : LS exp RE
               | empty'''

def p_attribute_call(p):
    '''attribute_call : ID DOT ID'''

def p_simple_id(p):
    '''simple_id : ID
                 | attribute_call'''

def p_function_return(p):
    '''function_return : LB RETURN LP EXPRESSION RP SEMI RB '''

def p_void_function_call(p):
    '''void_function_call : simple_id LP params_call RP SEMI'''

def p_params_call(p):
    '''params_call : expression params_call1'''

def p_params_call1(p):
    '''params_call1 : 
                    | COMMA expression'''

def p_read(p):
    '''read : READ LP read1 RP SEMI'''

def p_read1(p):
    '''read1 : var_id read2'''

def p_read2(p):
    '''read2 :
             | COMMA VAR_ID read2'''

def p_write(p):
    '''write : WRITE LP write_params RP SEMI'''

def p_write_params(p):
    '''write_params : write_params1 write_params2'''

def p_write_params1(p):
    '''write_params1 : expression | CTES '''

def p_write_params2(p):
    '''write_params2 : write_params | empty'''

def p_if(p):
    '''if : IF LP expression RP THEN block else'''

def p_else(p):
    '''else :
            | ELSE block'''
             
def p_block(p): 
    '''block : LB statement SEMI block1 RB '''

def p_block1(p):
    '''block1 :  
              | statement block1'''

def p_while(p):
    '''while : WHILE LP expression LB DO block'''

def p_from(p):
    '''from : FROM ID EQ expression UNTIL expression DO block'''

def p_expression(p):
    '''expression : exp expression1'''

def p_expression1(p):
    '''expression1 : 
                   | expression2 exp'''

def p_expression2(p):
    '''expression2 : GT
                   | LT
                   | GT EQ
                   | LT EQ
                   | EQ EQ
                   | EXCLAMATION EQ'''

def p_exp(p):
    '''exp : term exp2'''

def p_exp2(p):
    '''exp2 : 
            | exp3 term'''

def p_exp3(p):
    '''exp3 : PLUS
            | MINUS'''
             
def p_term(p): 
    '''term : factor term2'''

def p_term2(p):
    '''term2 : 
             | term3 factor'''

def p_term3(p):
    '''term3 : MUL
             | DIV'''

def p_factor(p):
    '''factor : LP expression RP
              | factor2'''

def p_factor1(p):
    '''factor1 : factor2 var_cte'''

def p_factor2(p):
    '''factor2 :
               |  PLUS
               | MINUS'''

def p_var_cte(p):
    '''var_cte : var_id
               | INT
               | FLOAT
               | CHAR
               | func_call'''

def p_func_call(p):
    '''func_call : func_call1 LP params_call RP'''

def p_func_call1(p):
    ''' func_call1 : ID
                   | ID DOT ID'''


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

