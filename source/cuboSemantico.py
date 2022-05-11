# leftOp, rightOp, operator, resultType
# bool con lógica entera (0 y 1)
cuboSemantico = {
    'int':{
        'int':{
            '*': 'int',
            '/': 'int',
            '+': 'int',
            '-': 'int',
            '<': 'int',
            '<=': 'int',
            '>': 'int',
            '>=': 'int',
            '==': 'int',
            '!=': 'int',
            '&': 'int',
            '||': 'int',
            '=': 'int'
        },
        'float':{
            '*': 'float',
            '/': 'float',
            '+': 'float',
            '-': 'float',
            '<': 'int',
            '<=': 'int',
            '>': 'int',
            '>=': 'int',
            '==': 'int',
            '!=': 'int',
            '&': 'int',
            '||': 'int',
            '=': 'ERROR'
        },
        'char':{
            '*': 'ERROR',
            '/': 'ERROR',
            '+': 'ERROR',
            '-': 'ERROR',
            '<': 'ERROR',
            '<=': 'ERROR',
            '>': 'ERROR',
            '>=': 'ERROR',
            '==': 'ERROR',
            '!=': 'ERROR',
            '&': 'ERROR',
            '||': 'ERROR',
            '=': 'ERROR'
        }
    },
    'float':{
        'int':{
            '*': 'float',
            '/': 'float',
            '+': 'float',
            '-': 'float',
            '<': 'int',
            '<=': 'int',
            '>': 'int',
            '>=': 'int',
            '==': 'int',
            '!=': 'int',
            '&': 'int',
            '||': 'int',
            '=': 'ERROR'
        },
        'float':{
            '*': 'float',
            '/': 'float',
            '+': 'float',
            '-': 'float',
            '<': 'int',
            '<=': 'int',
            '>': 'int',
            '>=': 'int',
            '==': 'int',
            '!=': 'int',
            '&': 'int',
            '||': 'int',
            '=': 'float'
        },
        'char':{
            '*': 'ERROR',
            '/': 'ERROR',
            '+': 'ERROR',
            '-': 'ERROR',
            '<': 'ERROR',
            '<=': 'ERROR',
            '>': 'ERROR',
            '>=': 'ERROR',
            '==': 'ERROR',
            '!=': 'ERROR',
            '&': 'ERROR',
            '||': 'ERROR',
            '=': 'ERROR'
        }
    },
    'char':{
        'int':{
            '*': 'ERROR',
            '/': 'ERROR',
            '+': 'ERROR',
            '-': 'ERROR',
            '<': 'ERROR',
            '<=': 'ERROR',
            '>': 'ERROR',
            '>=': 'ERROR',
            '==': 'ERROR',
            '!=': 'ERROR',
            '&': 'ERROR',
            '||': 'ERROR',
            '=': 'ERROR'
        },
        'float':{
            '*': 'ERROR',
            '/': 'ERROR',
            '+': 'ERROR',
            '-': 'ERROR',
            '<': 'ERROR',
            '<=': 'ERROR',
            '>': 'ERROR',
            '>=': 'ERROR',
            '==': 'ERROR',
            '!=': 'ERROR',
            '&': 'ERROR',
            '||': 'ERROR',
            '=': 'ERROR'
        },
        'char':{
            '*': 'ERROR',
            '/': 'ERROR',
            '+': 'ERROR',
            '-': 'ERROR',
            '<': 'ERROR',
            '<=': 'ERROR',
            '>': 'ERROR',
            '>=': 'ERROR',
            '==': 'int',
            '!=': 'int',
            '&': 'ERROR',
            '||': 'ERROR',
            '=': 'char'
        }
    }
}

def validateOperation(leftOp, rightOp, operator):
    if leftOp in cuboSemantico: # buscar izquierdo
        if rightOp in cuboSemantico[leftOp]: # buscar derecho
            if operator in cuboSemantico[leftOp][rightOp]: # buscar operador
                result = cuboSemantico[leftOp][rightOp][operator]
            else:
                print("ERROR: operator", operator, "not found.") # no se encontro operador
                exit()
        else:
            print("ERROR: right operand", rightOp, "not found.") # no se encontro derecho
            exit()
    else:
        print("ERROR: left operand", leftOp, "not found.") # no se encontro izquierdo
        exit()
    return result # OPERACION VALIDA

#------------------------------------TESTING------------------------------------
# while True:
#     left = input("leftOp: ")
#     operator = input("operator: ")
#     right = input("rightOp: ")
#
#     res = validateOperation(left,right,operator)
#     print(left, operator, right, "=", res)