import cuboSemantico as sc
import Variables as v

quadruples = []
registers = []
register_counter = 0
context = None

def expression(op, t1, t2, r):
    '''Creates quadruples for expressions that require a left
    and a right operand'''
    global register_counter
    r = 't' + str(register_counter)

    if t1 is None:
        t1 = registers[-1]
    if t2 is None:
        t2 = registers[-1]

    t1_type = None
    # TODO: Fow now handles
    # if its in the context, its a variable
    # otherwise its a constant
    if t1 in context:
        t1_type = context[t1].type
    elif t1 in registers:
        t1_type = t1[1]
    else:
        t1_type = type(t1).__name__
        # TODO: ERROR if it doesn't make sense (undeclared var, etc)

    t2_type = None
    if t2 in context:
        t2_type = context[t2].type
    elif t1 in registers:
        t2_type = t2[1]
    else:
        t2_type = type(t2).__name__
        # TODO: ERROR if it doesn't make sense (undeclared var, etc)

    r_type = sc.validateOperation(t1_type, t2_type, op)
    r = (r, r_type)
    registers.append(r)

    register_counter += 1

    quadruples.append((op, str(t1), str(t2), r))
    
def output_quadruples():
    with open("intermediate.out", "w") as o:
        for i in quadruples:
            o.write(i[0] + '\t' + i[1] + '\t' + i[2] + '\t' + i[3][0])
            o.write('\n')

def set_current_context(c):
    global context
    context = c