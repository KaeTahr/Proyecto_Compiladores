import sys
import vm_interpret as interpreter


def interpret(quad):
    op = int(quad[0])
    left_operand = quad[1]
    right_operand = quad[2]
    target = quad[3]
    interpreter.op_codes[op](left_operand, right_operand, target)




def main(ovejota):
    lines = open(ovejota, "r").readlines()
    for l in lines:
        quad = l.strip().split(',')
        interpret(quad)

if __name__ == '__main__':
    main(sys.argv[1])