from dirFunciones import FuncAttr, directorio_funciones, FuncAttr
from memoria import *
from tablaObjetos import tabla_obj


# AGREGAR VARIABLE A TABLA DE VARIABLES


def add_variable(var_id, var_type, var_kind, scope):
    if scope in directorio_funciones:  # buscar scope en directorio de funciones

        if var_id in directorio_funciones[scope][FuncAttr.VAR_TABLE]:
            print("ERROR: variable", var_id, "already exists in scope:", scope)
            exit()

        else:
            if directorio_funciones[scope][FuncAttr.RETURN_TYPE] == "program":
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
    print("Type:", directorio_funciones[scope][FuncAttr.VAR_TABLE][var_id][0])
    print("Kind:", directorio_funciones[scope][FuncAttr.VAR_TABLE][var_id][1])
    print("Address:", directorio_funciones[scope][FuncAttr.VAR_TABLE][var_id][2])
    print("---------------------------------------------------------------")


def print_var_table():
    for scope in directorio_funciones:
        if directorio_funciones[scope][FuncAttr.VAR_TABLE] != {}:  # que tenga variables definidas
            if directorio_funciones[scope][0] == "program":  # global
                print("\nVariables table for PROGRAM", scope)
            else:
                print("\nVariables table for FUNCTION", scope)
            for var in directorio_funciones[scope][FuncAttr.VAR_TABLE]:
                print("ID:", var, "\tType:", directorio_funciones[scope][FuncAttr.VAR_TABLE][var][0], "\tKind:",
                      directorio_funciones[scope][2][var][1], "\tAddress:", directorio_funciones[scope][FuncAttr.VAR_TABLE][var][2])
            print("---------------------------------------------------------------")


def instantiate_obj(var_id, class_id, scope):
    parent = tabla_obj[class_id]['parent']
    if tabla_obj[class_id]['attributes']:
        for attr in tabla_obj[class_id]['attributes']:
            name = str(var_id + "." + attr)
            var_type = tabla_obj[class_id]['attributes'][attr]
            add_variable(name, var_type, 'attribute', scope)

    if parent:
        if tabla_obj[parent]['attributes']:
            for attr in tabla_obj[parent]['attributes']:
                name = str(var_id + "." + attr)
                var_type = tabla_obj[parent]['attributes'][attr]
                add_variable(name, var_type, 'attribute', scope)
