from enum import IntEnum

directorio_funciones = {}

# functions are stored as a list:
# fun[0] = return type
# fun[1] = kind (global) or not
# fun[2] = local variable table
# fun[3] = parameters
# fun[4] = amount of temporary variables
# fun[5] = quadruple num where fun starts


class FuncAttr(IntEnum):
    RETURN_TYPE = 0
    IS_GLOBAL = 1
    VAR_TABLE = 2
    PARAMETERS = 3
    TEMP_AMOUNT = 4
    START = 5

def get_dir_funciones():
    return directorio_funciones

# agregar funcion a directorio de funciones
def add_function(fun_id, fun_type, kind):
    if fun_id in directorio_funciones:  # funcion ya existe
        print("ERROR: function", fun_id, "already exists in function directory.")
        exit()

    else:
        directorio_funciones[fun_id] = [fun_type, kind, {}, (), 0, -1]


def new_function_log(fun_id):
    print("\n-------------------------FUNCTION----------------------------------")
    print('New entry in function directory:')
    print("ID:", fun_id, "\tType:",
          directorio_funciones[fun_id][FuncAttr.RETURN_TYPE], "\tKind:", directorio_funciones[fun_id][FuncAttr.IS_GLOBAL], "\n")
    print('at quadruple: ', directorio_funciones[fun_id][FuncAttr.START])


def clear_function_directory():
    directorio_funciones.clear()


def get_var_type(var_id, scope):
    first = list(directorio_funciones.keys())[
        0]  # referencia a variables globales

    # buscar en scope especificado
    if var_id in directorio_funciones[scope][FuncAttr.VAR_TABLE]:
        # print("Variable", id, "found within scope", scope)
        return directorio_funciones[scope][FuncAttr.VAR_TABLE][var_id][0]

    elif var_id in directorio_funciones[first][FuncAttr.VAR_TABLE]:  # buscar en scope global
        # print("Variable", id, "found within GLOBAL scope", first)
        return directorio_funciones[first][FuncAttr.VAR_TABLE][var_id][0]

    else:  # no se encontro la variable
        print("ERROR: variable", var_id, "not found.")
        exit()


def get_var_address(var_id):
    for scope in directorio_funciones:
        if var_id in directorio_funciones[scope][FuncAttr.VAR_TABLE]:
            return directorio_funciones[scope][FuncAttr.VAR_TABLE][var_id][2]


def sign_function(id):
    parameters =  directorio_funciones[id][FuncAttr.VAR_TABLE]
    parameters = tuple(i[0] for i in list(parameters.values()))
    directorio_funciones[id][FuncAttr.PARAMETERS] = parameters

def get_fun_signature(id):
    if id in directorio_funciones:
        f = directorio_funciones[id]
        return (f[FuncAttr.RETURN_TYPE], id,  f[FuncAttr.PARAMETERS])
    else:
        print("ERROR: Attempted to call undefined function")
        exit()

def fun_start(id, ip):
    f = directorio_funciones[id]
    f[FuncAttr.START] = ip
    # new_function_log(id) # log info

def set_local_tmp_count(id, tmp_count):
    f = directorio_funciones[id]
    f[FuncAttr.TEMP_AMOUNT] = tmp_count