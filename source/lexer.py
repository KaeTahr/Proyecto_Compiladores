import ply.lex as lex

# reserved words
reserved = {
    'program': 'PROGRAM',
    'main': 'MAIN',
    'class': 'CLASS',
    'inherits': 'INHERITS',
    'attributes': 'ATTRIBUTES',
    'methods': 'METHODS',
    'variables': 'VARIABLES',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'read': 'READ',
    'write': 'WRITE',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'from': 'FROM',
    'until': 'UNTIL',
    'void': 'VOID'
}

# tokens
tokens = [
             'PLUS', 'MIN', 'MUL', 'DIV',
             'LT', 'GT', 'GTE', 'LTE',
             'COMP', 'NE',
             'EQ',
             'OR', 'AND',
             'LB', 'RB',
             'LP', 'RP',
             'LS', 'RS',
             'COMMA', 'DOT',
             'SEMI',
             'COLON',
             'ID',
             'CTEI', 'CTEF', 'CTES', 'CTEC'
         ] + list(reserved.values())

# IGNORED CHARACTERS
t_ignore = ' \t\n'

# Comments
t_ignore_COMMENT = r'\#.*'

# OPERATORS
t_PLUS = r'\+'
t_MIN = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_LT = r'<'
t_GT = r'>'
t_COMP = r'=='
t_NE = r'!='
t_OR = r'\|\|'
t_AND = r'&'
t_GTE = r'>='
t_LTE = r'<='

# ASSIGNMENT
t_EQ = r'='

# BRACKET
t_LB = r'\{'
t_RB = r'\}'

# PARENTHESIS
t_LP = r'\('
t_RP = r'\)'

# SQUARE
t_LS = r'\['
t_RS = r'\]'

t_COMMA = r','
t_SEMI = r';'
t_COLON = r':'
t_DOT = r'\.'

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