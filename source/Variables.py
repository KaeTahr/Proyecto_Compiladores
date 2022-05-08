from enum import Enum

var_table = []
var_counter = 0

class Types(Enum):
    INT = 1
    CHAR = 2
    FLOAT = 3

class Var:
    '''Variable Class
    attributes: id - string
                type - 1, 2, or 3 according to Type Enum
                value - corresponds to type
    methods:'''
    def __init__(self, id, type):
        '''Initialize Variable object'''
        self.id = id
        self.type = type
        self.value = None
        # self.validate_type()
        # var_table.append(self)
    
    def assign(self, value):
        self.value = value

    def validate_type(self):
        if self.type is Types.INT:
            if type(self.value) is not int:
                raise TypeError('error in type matching')
        elif self.type is Types.CHAR:
            if type(self.value) is not int:
                raise TypeError('error in type matching')
        elif self.type is Types.FLOAT:
            if type(self.value) != float:
                raise TypeError('error in type matching')
        else:
            raise TypeError('unknown type: ' + self.type)


def str_to_enum(type_str):
    if type_str == 'int':
        return Types.INT
    elif type_str == 'float':
        return Types.FLOAT
    elif type_str == 'char':
        return Types.CHAR
    else:
        return -1

def newVariableLog(id, type):
    print("!!!Variable!!!")
    print("new entry in current context")
    print("ID:", id, "\ttype:", type)

#--------------------TESTING----------------
""" while True:
    id = input("id: ")
    v = input("value: ") #string from stdin
    t = input("type: ")

    t = str_to_enum(t)

    v = Var(id, v, t)
    print(v)
    print(var_table) """