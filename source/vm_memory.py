from enum import IntEnum

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

dir_fun = {}

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
        print(v)
        if r == contextRanges.INT:
            v = int(v)
        elif r == contextRanges.FLOAT:
            v = float(v)
        memory[c][r].append(v)

def initiate_temporary_variables(t):
    c = memoryContext.TEMPORAL
    memory[c][contextRanges.INT] = [None] * t[0]
    memory[c][contextRanges.FLOAT] = [None] * t[0]
    memory[c][contextRanges.CHAR] = [None] * t[0]

def initiate_global_variables(t):
    c = memoryContext.GLOBAL
    memory[c][contextRanges.INT] = [None] * t[0]
    memory[c][contextRanges.FLOAT] = [None] * t[0]
    memory[c][contextRanges.CHAR] = [None] * t[0]

def initiate_functions(func_list):
    for i in range(0, len(func_list), 7):
        id = func_list[i]
        ints = int(func_list[i+1])
        floats = int(func_list[i+2])
        chars = int(func_list[i+3])
        t_ints = int(func_list[i+4])
        t_floats = int(func_list[i+5])
        t_chars = int(func_list[i+6])
        dir_fun[id] = [(ints, floats, chars), (t_ints, t_floats, t_chars)]
    
    initiate_global_variables(dir_fun[func_list[0]][0])
    initiate_temporary_variables(dir_fun[func_list[0]][1])

    