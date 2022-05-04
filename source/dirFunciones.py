dirFunctions = {}
current_fun_id = ''
current_fun_type = ''
current_var_id = ''
current_var_type = ''
typeStack = []
newVarType = False

# agregar funcion a directorio de funciones
def addFunction(kind):
    if current_fun_id in dirFunctions: # funcion ya existe
        print("ERROR: function", current_fun_id, "already exists in function directory.")
        exit()
    else:
        dirFunctions[current_fun_id] = [current_fun_type, kind, {}]
        newFunctionLog() # log info


def addVariable(kind):
    if current_fun_id in dirFunctions: # buscar funcion en directorio de funciones
        if current_var_id in dirFunctions[current_fun_id][2]: # buscar variable en scope actual
            print("ERROR: variable", current_var_id, "already exists in scope:", current_fun_id)
            exit()
        else:
            dirFunctions[current_fun_id][2][current_var_id] = [current_var_type, kind] # agregar nueva variable
            newVariableLog() # log info
    else:
        print("ERROR: FUNCTION", current_fun_id, "NOT FOUND.\n") # no se encontro funcion
        exit()

def newFunctionLog():
    print("-------------------------FUNCTION----------------------------------")
    print('New entry in function directory:')
    print("ID:", current_fun_id, "\tType:", dirFunctions[current_fun_id][0], "\tKind:", dirFunctions[current_fun_id][1])
    print("-------------------------VARIABLES---------------------------------")


def newVariableLog():
    print('New entry in variable table for scope', current_fun_id)
    print("ID:", current_var_id, "\tType:", current_var_type, "\tKind:", dirFunctions[current_fun_id][2][current_var_id][1])


def clearFunctionDir():
    dirFunctions.clear()
    current_fun_id = ''
    current_fun_type = ''
    current_var_id = ''
    current_var_type = ''
    typeStack = []
    newVarType = False

#------------------------------------TESTING------------------------------------
# while True:
#     id = input('Enter function id: ')
#     type = input('Enter function type: ')
#     kind = input('Enter function kind: ')
#
#     addFunction(id,type,kind)
#
#     print('Function Directory: ', dirFunctions)