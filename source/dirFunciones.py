directorio_funciones = {}


# agregar funcion a directorio de funciones
def add_function(fun_id, fun_type, kind):
    if fun_id in directorio_funciones:  # funcion ya existe
        print("ERROR: function", fun_id, "already exists in function directory.")
        exit()

    else:
        directorio_funciones[fun_id] = [fun_type, kind, {}]
        #new_function_log(fun_id) # log info


def new_function_log(fun_id):
    print("\n-------------------------FUNCTION----------------------------------")
    print('New entry in function directory:')
    print("ID:", fun_id, "\tType:", directorio_funciones[fun_id][0], "\tKind:", directorio_funciones[fun_id][1], "\n")


def clear_function_directory():
    directorio_funciones.clear()
