from csv import excel_tab
from enum import IntEnum
from importlib.abc import ExecutionLoader

class memoryContext(IntEnum):
    GLOBAL = 0,
    LOCAL = 1,
    TEMPORAL = 2,
    CONSTANT = 3

class contextRanges(IntEnum):
    INT = 0,
    FLOAT = 1,
    CHAR = 2
    STRING = 3 # !! ONLY CONSTANTS CONTAIN THIS

class StackMemory(IntEnum):
    IP = 0,
    LOCAL_MEM = 1,
    TMP_MEM = 2,
    EXPECTING_RETURN = 3

class Df(IntEnum):
    ID = 0,
    LOCAL_MEM = 1,
    TMP_MEM = 2,
    RETURN_ADDRESS = 3

# fun_name: local_mem, tmp_mem, return_address
dir_fun = {}

# (quad_num [local_memory] awaitng_return_from_fun)
execution_stack = [] 
memory = [
    [ # global
        [], # int
        [], # float
        [], # char
    ], 

    [ # local
        [],
        [],
        [],
    ],

    [ # temporal
        [],
        [],
        [],
    ],

    [ # constant
        [], # int
        [], # float
        [], # char
        [], # string !! constants only
    ]
]

def memory_lookup(address):
    '''Given an address, returns a 3D tuple meant to be used to 
    access the memory map'''
    address = int(address)
    context = 0
    mem_range = 0
    t_address = address
    if address < 4000:
        context = memoryContext.GLOBAL
        t_address = address - 1000
    elif address >= 4000 and address < 7000:
        context = memoryContext.LOCAL
        t_address = address - 4000
    elif address >= 7000 and address < 10000:
        context = memoryContext.TEMPORAL
        t_address = address - 7000
    elif address >= 10000 and address < 13000:
        context = memoryContext.CONSTANT
        t_address = address - 10000
    elif address >= 13000 and address < 14000: # special string constant
        context = memoryContext.CONSTANT
        return context, contextRanges.STRING, address - 13000, 
    else:
        raise MemoryError("overflow")

    if t_address >= 0 and t_address < 1000:
        mem_range = contextRanges.INT
        # t_address -= 0
    elif t_address >= 1000 and t_address < 2000:
        mem_range = contextRanges.FLOAT
        t_address -=  1000
    elif t_address >= 2000 and t_address < 3000:
        mem_range = contextRanges.CHAR
        t_address -= 2000
    else:
        raise MemoryError("overflow")
        
    return context, mem_range, t_address

def memory_read(address):
    c, r, off = memory_lookup(address)
    return memory[c][r][off]

def memory_write(value, address):
    c, r, off = memory_lookup(address)
    if r == contextRanges.INT:
        value = int(value)
    elif r == contextRanges.FLOAT:
        value = float(value)
    memory[c][r][off] = value

def initiate_constants(constant_list):
    while constant_list:
        v = constant_list.pop(0)
        a = int(constant_list.pop(0))
        c, r, off = memory_lookup(int(a))
        if r == contextRanges.INT:
            v = int(v)
        elif r == contextRanges.FLOAT:
            v = float(v)
        memory[c][r].append(v)

def initiate_temporary_variables(t):
    c = memoryContext.TEMPORAL
    memory[c][contextRanges.INT] = [None] * t[0]
    memory[c][contextRanges.FLOAT] = [None] * t[1]
    memory[c][contextRanges.CHAR] = [None] * t[2]

def initiate_global_variables(t):
    c = memoryContext.GLOBAL
    memory[c][contextRanges.INT] = [None] * t[0]
    memory[c][contextRanges.FLOAT] = [None] * t[1]
    memory[c][contextRanges.CHAR] = [None] * t[2]

def initiate_functions(func_list):
    for i in range(0, len(func_list), 8):
        id = func_list[i]
        ints = int(func_list[i+1])
        floats = int(func_list[i+2])
        chars = int(func_list[i+3])
        t_ints = int(func_list[i+4])
        t_floats = int(func_list[i+5])
        t_chars = int(func_list[i+6])
        return_address = int(func_list[i+7])
        dir_fun[id] = [(ints, floats, chars), (t_ints, t_floats, t_chars), return_address]
    
    initiate_global_variables(dir_fun[func_list[0]][0])
    initiate_temporary_variables(dir_fun[func_list[0]][1])

def prepare_context(function):
    f = dir_fun[function]
    new_context_local = [[], [], []]
    new_context_tmp = [[], [], []]
    new_context_local[contextRanges.INT] = [None] * f[0][0]
    new_context_local[contextRanges.FLOAT] = [None] * f[0][1]
    new_context_local[contextRanges.CHAR] = [None] * f[0][2]
    new_context_tmp[contextRanges.INT] = [None] * f[1][0]
    new_context_tmp[contextRanges.FLOAT] = [None] * f[1][1]
    new_context_tmp[contextRanges.CHAR] = [None] * f[1][2]
    execution_stack.append([-1, new_context_local, new_context_tmp])

def handle_param(address, param_num):
    c, r, off = memory_lookup(address)
    v = memory[c][r][off]
    off = param_num - 1
    found = False
    while not found:
        if off == 0:
            found = True
        elif execution_stack[-1][StackMemory.LOCAL_MEM][r][off - 1] == None:
            off -= 1
        else:
            found = True
    execution_stack[-1][1][r][off] = v

def start_subroutine(fun, ip):
    c = execution_stack.pop()
    prev_memory = memory[memoryContext.LOCAL].copy()
    prev_tmp = memory[memoryContext.TEMPORAL].copy()
    prev = [ip, prev_memory, prev_tmp, fun]
    execution_stack.append(prev)
    memory[memoryContext.LOCAL] = c[StackMemory.LOCAL_MEM]
    memory[memoryContext.TEMPORAL] = c[StackMemory.TMP_MEM]

def end_subroutine(value_address):
    prev = execution_stack.pop()
    value = memory_read(value_address)
    memory[memoryContext.LOCAL] = prev[1]
    memory[memoryContext.TEMPORAL] = prev[2]
    f = prev[3]
    address = dir_fun[f][2]
    memory_write(value, address)
    return prev[0]
