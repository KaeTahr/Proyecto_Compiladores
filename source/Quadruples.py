quadruples = []
registers = []
register_counter = 0

def expression(op, t1, t2, r):
    '''Creates quadruples for expressions that require a left
    and a right operand'''
    global register_counter
    r = 't' + str(register_counter)
    registers.append(r)

    register_counter += 1

    if t1 is None:
        t1 = registers[-2]
    if t2 is None:
        t2 = registers[-2]

    quadruples.append((op, str(t1), str(t2), r))
    
def output_quadruples():
    with open("intermediate.out", "w") as o:
        for i in quadruples:
            o.write(i[0] + '\t' + i[1] + '\t' + i[2] + '\t' + i[3])
            o.write('\n')