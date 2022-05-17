directorio_funciones = {}


# agregar funcion a directorio de funciones
def add_function(fun_id, fun_type, kind):
    if fun_id in directorio_funciones:  # funcion ya existe
        print("ERROR: function", fun_id, "already exists in function directory.")
        exit()

    else:
        directorio_funciones[fun_id] = [fun_type, kind, {}]
        # new_function_log(fun_id) # log info


def new_function_log(fun_id):
    print("\n-------------------------FUNCTION----------------------------------")
    print('New entry in function directory:')
    print("ID:", fun_id, "\tType:", directorio_funciones[fun_id][0], "\tKind:", directorio_funciones[fun_id][1], "\n")


def clear_function_directory():
    directorio_funciones.clear()


def get_var_type(var_id, scope):
    first = list(directorio_funciones.keys())[0]  # referencia a variables globales

    if var_id in directorio_funciones[scope][2]:  # buscar en scope especificado
        # print("Variable", id, "found within scope", scope)
        return directorio_funciones[scope][2][var_id][0]

    elif var_id in directorio_funciones[first][2]:  # buscar en scope global
        # print("Variable", id, "found within GLOBAL scope", first)
        return directorio_funciones[first][2][var_id][0]

    else:  # no se encontro la variable
        print("ERROR: variable", var_id, "not found.")
        exit()


def get_var_address(var_id):
    for scope in directorio_funciones:
        if var_id in directorio_funciones[scope][2]:
            return directorio_funciones[scope][2][var_id][2]
