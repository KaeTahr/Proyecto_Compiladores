import sys
import vm_memory as m

ip = 0

def get_ip():
    global ip
    return ip - 1

def set_ip(target):
    global ip
    ip = target

def ip_continue():
    global ip
    ip += 1

def mult(lo, ro, t):
    ip_continue()
    pass

def div(lo, ro, t):
    ip_continue()
    pass

def add(lo, ro, t):
    ip_continue()
    pass

def subtract(lo, ro, t):
    ip_continue()
    pass

def lt(lo, ro, t):
    ip_continue()
    pass

def gt(lo, ro, t):
    ip_continue()
    pass

def equal(lo, ro, t):
    ip_continue()
    pass

def not_equal(lo, ro, t):
    ip_continue()
    pass

def gte(lo, ro, t):
    ip_continue()
    pass

def lte(lo, ro, t):
    pass

def and_et(lo, ro, t):
    ip_continue()
    pass

def or_vel(lo, ro, t):
    ip_continue()
    pass

def assign(lo, ro, t):
    ip_continue()

def ret(lo, ro, t):
    ip_continue()
    pass

def read(lo, ro, t):
    ip_continue()
    pass

def write(lo, ro, t):
    o = m.memory_read(int(t))
    print(o)
    ip_continue()

op_codes = [
    mult, # 0
    div, # 1
    add, # 2
    subtract, # 3
    lt, # 4
    gt, #5
    equal,
    not_equal,
    gte,
    lte,
    and_et,
    or_vel,
    assign,
    ret,
    read,
    write,
    # TODO: Complete this list
]

def eval(quad):
    op = quad.pop(0)
    op = int(op)
    left_operand = quad[0]
    right_operand = quad[1]
    target = quad[2]
    op_codes[op](left_operand, right_operand, target)


def main(ovejota):
    lines = open(ovejota, "r").readlines()
    while (ip < len(lines)): 
        quad = l.strip().split(',')
        if ip == 0:
            quad.pop(0)
            m.initiate_constants(quad)
        elif ip == 1:
            quad.pop(0)
            m.inititate_var_table(quad)
        l = lines[ip]
        eval(quad)

if __name__ == '__main__':
    main(sys.argv[1])