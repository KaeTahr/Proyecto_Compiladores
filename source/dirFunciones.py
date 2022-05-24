from tablaObjetos import *

directorio_funciones = {}


# add function to function directory
def add_function(fun_id, fun_type, kind):
    if fun_id in directorio_funciones:  # function already exists
        print("ERROR: function", fun_id, "already exists in function directory.")
        exit()

    else:
        directorio_funciones[fun_id] = [fun_type, kind, {}]
        # new_function_log(fun_id) # log info


def new_function_log(fun_id):
    print("\n-------------------------FUNCTION----------------------------------")
    print('New entry in function directory:')
    print("ID:", fun_id, "\tType:", directorio_funciones[fun_id][0], "\tKind:", directorio_funciones[fun_id][1], "\n")


def get_var_type(var_id, scope, curr_class):
    first = list(directorio_funciones.keys())[0]  # reference to global scope
    if curr_class:
        parent = tabla_obj[curr_class]['parent']  # check if class is child of another

    if var_id in directorio_funciones[scope][2]:  # search in local scope
        # print("Variable", id, "found within scope", scope)
        return directorio_funciones[scope][2][var_id][0]

    elif var_id in directorio_funciones[first][2]:  # search in global scope
        # print("Variable", id, "found within GLOBAL scope", first)
        return directorio_funciones[first][2][var_id][0]

    elif var_id in tabla_obj[curr_class]['attributes']:  # search in object attributes
        return tabla_obj[curr_class]['attributes'][var_id]

    elif parent and var_id in tabla_obj[parent]['attributes']:  # search in parent class attributes
        return tabla_obj[parent]['attributes'][var_id]

    else:  # variable was not found
        print("ERROR: variable", var_id, "not found in scope", scope)
        exit()


def get_var_address(var_id):
    for scope in directorio_funciones:
        if var_id in directorio_funciones[scope][2]:
            return directorio_funciones[scope][2][var_id][2]
