import Variables

dirFunctions = {}
curr_id = None

# agregar funcion a directorio de funciones
def addFunction(id,type,kind):
    global curr_id
    if id in dirFunctions: # funcion ya existe
        print("ERROR: function", id, "already exists in function directory.")
        exit()
    else:
        dirFunctions[id] = [type, kind, {}]
        curr_id = id
        newFunctionLog(id) # log info

def addVarsToContext(id_list, type):
    for i in id_list:
        if '[' in i:
            continue # TODO: Skip arrays for now, we need to handle them
        addVarToContext(i, type)

def addVarToContext(id, type):
        tmp_var = Variables.Var(id, type)
        dirFunctions[curr_id][2][id] = tmp_var
        Variables.newVariableLog(id, type)


def newFunctionLog(id):
    print("\n-------------------------FUNCTION----------------------------------")
    print('New entry in function directory:')
    print("ID:", id, "\tType:", dirFunctions[id][0], "\tKind:", dirFunctions[id][1], "\n")


def clearFunctionDir():
    dirFunctions.clear()


#------------------------------------TESTING------------------------------------
# while True:
#     id = input('Enter function id: ')
#     type = input('Enter function type: ')
#     kind = input('Enter function kind: ')
#
#     addFunction(id,type,kind)