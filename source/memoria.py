addr_range = 1000

virtual_memory = {
    'global': {
        'int': {'initial': 1000, 'count': 0},
        'float': {'initial': 2000, 'count': 0},
        'char': {'initial': 3000, 'count': 0},
        'object' : {'initial': 4000, 'count': 0}
    },
    'local': {
        'int': {'initial': 5000, 'count': 0},
        'float': {'initial': 6000, 'count': 0},
        'char': {'initial': 7000, 'count': 0},
        'object' : {'initial': 8000, 'count': 0}
    },
    'temporal': {
        'int': {'initial': 9000, 'count': 0},
        'float': {'initial': 10000, 'count': 0},
        'char': {'initial': 11000, 'count': 0},
        'pointer': {'initial': 50000, 'count': 0}
    },
    'constant': {
        'int': {'initial': 12000, 'count': 0},
        'float': {'initial': 13000, 'count': 0},
        'char': {'initial': 14000, 'count': 0},
        'string': {'initial': 15000, 'count': 0}
    }
}

valid_types = ['int', 'char', 'float', 'string', 'pointer', 'object']


def get_avail(scope, v_type):
    '''Basically, malloc() for our compiler.
    Asks for new memory given:
    - scope (global, local, temporal, consant)
    - type (int, float, char, string, pointer)'''
    if v_type in valid_types:
        assigned_addr = virtual_memory[scope][v_type]['initial'] + virtual_memory[scope][v_type]['count']
        if assigned_addr < virtual_memory[scope][v_type]['initial'] + addr_range:
            virtual_memory[scope][v_type]['count'] += 1  # update count
            return assigned_addr
        else:
            print("ERROR: Too many", scope, " variables of type", v_type)
            exit()


def get_avail_1(scope, v_type):
    if v_type in valid_types:
        assigned_addr = virtual_memory[scope][v_type]['initial'] + virtual_memory[scope][v_type]['count']
        if assigned_addr < virtual_memory[scope][v_type]['initial'] + addr_range:
            return assigned_addr
        else:
            print("ERROR: Too many", scope, " variables of type", v_type)
            exit()


def get_count(scope, v_type):
    '''Gets the amount of used variables, given a scope and a type'''
    current_avail = virtual_memory[scope][v_type]['count']
    return current_avail


def reset_local():
    '''Clears local memory, for when defining a new context'''
    global virtual_memory
    virtual_memory['local']['int']['count'] = 0
    virtual_memory['local']['float']['count'] = 0
    virtual_memory['local']['char']['count'] = 0


def reset_temp():
    '''Clears temporary memory, for when defining a new context'''
    global virtual_memory
    virtual_memory['temporal']['int']['count'] = 0
    virtual_memory['temporal']['float']['count'] = 0
    virtual_memory['temporal']['char']['count'] = 0
    virtual_memory['temporal']['pointer']['count'] = 0


def update_avail(v_type, scope, size):
    '''Corrects next available memory, necessary when creating arrays or matrices'''
    global virtual_memory
    for i in range(1, size):
        virtual_memory[scope][v_type]['count'] += 1  # update count
