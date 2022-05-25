addr_range = 1000

virtual_memory = {
    'global': {
        'int': {'initial': 1000, 'count': 0},
        'float': {'initial': 2000, 'count': 0},
        'char': {'initial': 3000, 'count': 0}
    },
    'local': {
        'int': {'initial': 4000, 'count': 0},
        'float': {'initial': 5000, 'count': 0},
        'char': {'initial': 6000, 'count': 0}
    },
    'temporal': {
        'int': {'initial': 7000, 'count': 0},
        'float': {'initial': 8000, 'count': 0},
        'char': {'initial': 9000, 'count': 0},
        'bool': {'initial': 10000, 'count': 0}
    },
    'constant': {
        'int': {'initial': 11000, 'count': 0},
        'float': {'initial': 12000, 'count': 0},
        'char': {'initial': 13000, 'count': 0},
        'string': {'initial': 14000, 'count': 0}
    }
}

valid_types = ['int', 'char', 'float', 'bool', 'string']


def get_avail(scope, v_type):
    if v_type in valid_types:
        assigned_addr = virtual_memory[scope][v_type]['initial'] + virtual_memory[scope][v_type]['count']
        if assigned_addr < virtual_memory[scope][v_type]['initial'] + addr_range - 1:
            virtual_memory[scope][v_type]['count'] += 1  # update count
            return assigned_addr
        else:
            print("ERROR: Too many", scope, " variables of type", v_type)
            exit()


def get_count(scope, v_type):
    current_avail = virtual_memory[scope][v_type]['count']
    return current_avail


def reset_local():
    global virtual_memory
    virtual_memory['local']['int']['count'] = 0
    virtual_memory['local']['float']['count'] = 0
    virtual_memory['local']['char']['count'] = 0


def reset_temp():
    global virtual_memory
    virtual_memory['temporal']['int']['count'] = 0
    virtual_memory['temporal']['float']['count'] = 0
    virtual_memory['temporal']['char']['count'] = 0
    virtual_memory['temporal']['bool']['count'] = 0
