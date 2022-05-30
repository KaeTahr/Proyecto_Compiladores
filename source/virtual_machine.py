import sys
import vm_memory as m

TRUE = 1
FALSE = 0
ip = 0

def get_ip():
    global ip
    return ip - 1

def set_ip(target):
    global ip
    ip = target - 1

def ip_continue():
    global ip
    ip += 1

def mult(lo, ro, t):
    lo = m.memory_read(int(lo))
    ro = m.memory_read(int(ro))
    res = lo * ro
    m.memory_write(res, t)
    ip_continue()

def div(lo, ro, t):
    lo = m.memory_read(int(lo))
    ro = m.memory_read(int(ro))
    res = lo / ro
    m.memory_write(res, t)
    ip_continue()

def add(lo, ro, t):
    lo = m.memory_read(int(lo))
    ro = m.memory_read(int(ro))
    res = lo + ro
    m.memory_write(res, t)
    ip_continue()

def subtract(lo, ro, t):
    lo = m.memory_read(int(lo))
    ro = m.memory_read(int(ro))
    res = lo - ro
    m.memory_write(res, t)
    ip_continue()

def lt(lo, ro, t):
    lo = m.memory_read(int(lo))
    ro = m.memory_read(int(ro))
    res = lo < ro
    if res:
        res = TRUE
    else:
        res = FALSE
    m.memory_write(res, t)
    ip_continue()

def gt(lo, ro, t):
    lo = m.memory_read(int(lo))
    ro = m.memory_read(int(ro))
    res = lo > ro
    if res:
        res = TRUE
    else:
        res = FALSE
    m.memory_write(res, t)
    ip_continue()

def equal(lo, ro, t):
    lo = m.memory_read(int(lo))
    ro = m.memory_read(int(ro))
    res = lo == ro
    if res:
        res = TRUE
    else:
        res = FALSE
    m.memory_write(res, t)
    ip_continue()

def not_equal(lo, ro, t):
    lo = m.memory_read(int(lo))
    ro = m.memory_read(int(ro))
    res = lo != ro
    if res:
        res = TRUE
    else:
        res = FALSE
    m.memory_write(res, t)
    ip_continue()

def gte(lo, ro, t):
    lo = m.memory_read(int(lo))
    ro = m.memory_read(int(ro))
    res = lo >= ro
    if res:
        res = TRUE
    else:
        res = FALSE
    m.memory_write(res, t)
    ip_continue()

def lte(lo, ro, t):
    lo = m.memory_read(int(lo))
    ro = m.memory_read(int(ro))
    res = lo <= ro
    if res:
        res = TRUE
    else:
        res = FALSE
    m.memory_write(res, t)
    ip_continue()

def and_et(lo, ro, t):
    lo = m.memory_read(int(lo))
    ro = m.memory_read(int(ro))
    res = (lo == FALSE) and (ro == FALSE)
    if res:
        res = TRUE
    else:
        res = FALSE
    m.memory_write(res, t)
    ip_continue()

def or_vel(lo, ro, t):
    lo = m.memory_read(int(lo))
    ro = m.memory_read(int(ro))
    res = (lo == FALSE) or (ro == FALSE)
    if res:
        res = TRUE
    else:
        res = FALSE
    m.memory_write(res, t)
    ip_continue()

def assign(lo, ro, t):
    lo = m.memory_read(int(lo))
    m.memory_write(lo, t)
    ip_continue()

def ret(lo, ro, t):
    ip_continue()

def read(lo, ro, t):
    ip_continue()

def write(lo, ro, t):
    o = m.memory_read(t)
    print(o)
    ip_continue()

def goto(lo, ro, t):
    set_ip(int(t))

def gotof(lo, ro, t):
    lo = m.memory_read(int(lo))
    res = (lo == FALSE)
    if (res):
        set_ip(int(t))
    else:
        ip_continue()

def gotot(lo, ro, t):
    ip_continue()

def era(lo, ro, t):
    ip_continue()

def endfunc(lo, ro, t):
    ip_continue()

def parameter(lo, ro, t):
    ip_continue()

def gosub(lo, ro, t):
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
    goto,
    gotof,
    gotot,
    era,
    endfunc,
    parameter,
    gosub
    # TODO: Complete this list
]

def eval(quad):
    op = quad.pop(0)
    op = int(op)
    left_operand = quad[0]
    right_operand = quad[1]
    target = quad[2]
    op_codes[op](left_operand, right_operand, int(target))


def main(ovejota):
    lines = open(ovejota, "r").readlines()
    constants = lines.pop(0)
    quad = constants.strip().split(',')
    quad.pop(0)
    m.initiate_constants(quad)
    functions = lines.pop(0)
    quad = functions.strip().split(',')
    quad.pop(0)
    m.initiate_functions(quad)


    while (ip < len(lines)): 
        l = lines[ip]
        quad = l.strip().split(',')
        eval(quad)

if __name__ == '__main__':
    main(sys.argv[1])