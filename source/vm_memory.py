from enum import IntEnum

class memoryContext(IntEnum):
    GLOBAL = 0,
    LOCAL = 1,
    TEMPORAL = 1,
    CONSTANT = 2

class contextRanges(IntEnum):
    INT = 0,
    FLOAT = 1,
    CHAR = 2
    STRING = 3 # !! ONLY CONSTANTS CONTAIN THIS


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
        return context, contextRanges.STRING, address - 3000, 
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
    memory[c][r][off] = value
