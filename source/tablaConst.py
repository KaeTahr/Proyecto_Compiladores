from memoria import *

tabla_const = {}


def add_constant(value, const_type):
    if value not in tabla_const:
        address = get_avail('constant', const_type)
        tabla_const[value] = [const_type, address]
        new_constant_log(value)  # log info
    else:  # constante ya existe
        # pass
        print("Constant", value, "already exists in constants table.")


def new_constant_log(value):
    print('New entry in constants table:')
    print("Value:", value, "\tType:", tabla_const[value][0], "\tAddress:", tabla_const[value][1], "\n")

# while True:
#     t_const = input("Valor: ")
#     t_type = input("Type: ")
#     add_constant(t_const, t_type)

