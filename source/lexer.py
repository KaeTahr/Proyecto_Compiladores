import ply.lex as lex

# reserved words
reserved = {
    'program': 'PROGRAM',
    'main': 'MAIN',
    'class': 'CLASS',
    'inherits': 'INHERITS',
    'variables': 'VARIABLES',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'read': 'READ',
    'write': 'write',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'from': 'FROM',
    'until': 'UNTIL',
    'attributes': 'ATTRIBUTES',
    'methods': 'METHODS'
}

# tokens
tokens = [
             'EQ', 'GT', 'LT', 'COMP',
             'DOT',
             'PLUS', 'MIN', 'MUL', 'DIV',
             'AND', 'OR',
             'LB', 'RB',
             'LP', 'RP',
             'LS', 'RS',
             'SEMI', 'COLON', 'COMMA',
             'CTEI', 'CTEF', 'CTES', 'ID', 'CTEC'
         ] + list(reserved.values())

# A string containing ignored characters
t_ignore = ' \t\n'

# regex
t_PLUS = r'\+'
t_MIN = r'-'
t_MUL = r'\*'
t_DIV = r'/'

t_GT = r'>'
t_LT = r'<'
t_COMP = r'=='

t_AND = r'\&'
t_OR = r'\|'

t_DOT = r'\.'

t_EQ = r'='

t_LB = r'\{'
t_RB = r'\}'
t_LP = r'\('
t_RP = r'\)'
t_LS = r'\['
t_RS = r'\]'
t_COMMA = r','
t_SEMI = r';'
t_COLON = r':'

# CHAR
t_CTEC = r'\'([A-Za-z]|[0-9])\''

# STRING
t_CTES = r'\"([^\\\n]|(\\.))*?\"'

# ID
def t_ID(t):
    r'[A-Za-z][A-Za-z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# FLOAT
def t_CTEF(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# INT
def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
