from dirFunciones import FuncAttr, directorio_funciones, FuncAttr
from memoria import *
from tablaObjetos import tabla_obj


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
            directorio_funciones[scope][2][var_id] = [var_type, var_kind, address, False, []]
            return address
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
                      directorio_funciones[scope][2][var][1], "\tAddress:",
                      directorio_funciones[scope][FuncAttr.VAR_TABLE][var][2])
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


def set_array(var_id, scope):
    if var_id in directorio_funciones[scope][2]:
        directorio_funciones[scope][2][var_id][3] = True


def set_dim(var_id, scope, dim):
    directorio_funciones[scope][2][var_id][4].append(dim)


def arr_end(var_id, scope, g_scope):
    size = directorio_funciones[scope][2][var_id][4][0]
    # virtual_address = directorio_funciones[scope][2][var_id][2] + size - 1
    v_type = directorio_funciones[scope][FuncAttr.VAR_TABLE][var_id][0]
    if scope == g_scope:
        update_avail(v_type, 'global', size)
    else:
        update_avail(v_type, 'local', size)
    # print("Last address of", var_id, virtual_address)


def mat_end(var_id, scope, g_scope):
    size = directorio_funciones[scope][2][var_id][4][0] * directorio_funciones[scope][2][var_id][4][1]
    # virtual_address = directorio_funciones[scope][2][var_id][2] + size - 1
    v_type = directorio_funciones[scope][FuncAttr.VAR_TABLE][var_id][0]
    if scope == g_scope:
        update_avail(v_type, 'global', size)
    else:
        update_avail(v_type, 'local', size)
    # print("Last address of", var_id, virtual_address)
    # m is dim2 + 1


def verify_dim(var_id, scope, g_scope):
    if var_id in directorio_funciones[scope][2]:
        return directorio_funciones[scope][2][var_id][3]
    elif var_id in directorio_funciones[g_scope][2]:
        return directorio_funciones[g_scope][2][var_id][3]


def get_arr_dim(var_id, dim, scope, g_scope):
    if var_id in directorio_funciones[scope][2]:
        return directorio_funciones[scope][2][var_id][4][dim]

    elif var_id in directorio_funciones[g_scope][2]:
        return directorio_funciones[g_scope][2][var_id][4][dim]


def get_arr_m(var_id, scope, g_scope):
    if var_id in directorio_funciones[scope][2]:
        return directorio_funciones[scope][2][var_id][4][1] + 1

    elif var_id in directorio_funciones[g_scope][2]:
        return directorio_funciones[scope][2][var_id][4][1] + 1
