dirFunctions = {}

# agregar funcion a directorio de funciones
def addFunction(id,type,kind):
    if id in dirFunctions: # funcion ya existe
        print("ERROR: function", id, "already exists in function directory.")
        exit()
    else:
        dirFunctions[id] = [type, kind, {}]
        newFunctionLog(id) # log info


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