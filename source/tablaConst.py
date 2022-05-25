from memoria import *

tabla_const = {}

# lesser number, greater precedence
tabla_oper = {
    '*': 0,
    '/': 1,
    '+': 3,
    '-': 4,
    '<': 5,
    '>': 6,
    '==': 7,
    '!=': 8,
    '>=': 9,
    '<=': 10,
    '&': 11,
    '||': 12,
    '=': 13,
    'RETURN': 14,
    'READ': 15,
    'WRITE': 16,
    'GOTO': 17
}


def add_constant(value, const_type):
    if value not in tabla_const:
        address = get_avail('constant', const_type)
        tabla_const[value] = [const_type, address]
        # new_constant_log(value)  # log info
    else:  # constante ya existe
        pass
        # print("Constant", value, "already exists in constants table.")


def get_const_add(value):
    if tabla_const:
        return tabla_const[value][1]
    else:
        return 'undefined'


def get_const_type(value):
    if tabla_const:
        return tabla_const[value][0]
    else:
        return 'undefined'


def get_oper_code(operator):
    return tabla_oper[operator]


def new_constant_log(value):
    print('New entry in constants table:')
    print("Value:", value, "\tType:", tabla_const[value][0], "\tAddress:", tabla_const[value][1], "\n")


def print_const_table():
    if tabla_const:
        for key in tabla_const:
            print("Constants table")
            print("Value:", key, "\tType:", tabla_const[key][0], "\tAddress:", tabla_const[key][1])
        print("---------------------------------------------------------------")
