from dirFunciones import directorio_funciones
from memoria import *


# AGREGAR VARIABLE A TABLA DE VARIABLES
def add_variable(var_id, var_type, var_kind, scope):
    if scope in directorio_funciones:  # buscar scope en directorio de funciones

        if var_id in directorio_funciones[scope][2]:
            print("ERROR: variable", var_id, "already exists in scope:", scope)
            exit()

        else:
            if directorio_funciones[scope][0] == "program":
                address = get_avail("global", var_type)
            else:
                address = get_avail("local", var_type)
            directorio_funciones[scope][2][var_id] = [var_type, var_kind, address]
            # new_variable_log(var_id, scope)  # log info

    else:
        print("ERROR: FUNCTION", scope, "NOT FOUND.\n")  # no se encontro scope
        exit()


# LOG VARIABLES
def new_variable_log(var_id, scope):
    print('\nNew entry in variable table for scope', scope)
    print("ID:", var_id)
    print("Type:", directorio_funciones[scope][2][var_id][0])
    print("Kind:", directorio_funciones[scope][2][var_id][1])
    print("Address:", directorio_funciones[scope][2][var_id][2])
    print("---------------------------------------------------------------")


def print_var_table():
    for scope in directorio_funciones:
        if directorio_funciones[scope][2] != {}:  # que tenga variables definidas
            if directorio_funciones[scope][0] == "program":  # global
                print("\nVariables table for PROGRAM", scope)
            else:
                print("\nVariables table for FUNCTION", scope)
            for var in directorio_funciones[scope][2]:
                print("ID:", var, "\tType:", directorio_funciones[scope][2][var][0], "\tKind:",
                      directorio_funciones[scope][2][var][1], "\tAddress:", directorio_funciones[scope][2][var][2])
            print("---------------------------------------------------------------")
