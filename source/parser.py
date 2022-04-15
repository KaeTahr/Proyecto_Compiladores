import ply.yacc as yacc
from lexer import tokens
import sys


# PROGRAMA
def p_program(p):
    '''program : PROGRAM ID SEMI p1'''
    p[0] = "INPUT FILE ACCEPTED\n"



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

