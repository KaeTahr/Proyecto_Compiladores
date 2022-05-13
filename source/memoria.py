addr_range = 1000
first_avail = 0

virtual_memory = {
    'global': {
        'int': {'initial': first_avail + addr_range, 'count': 0},
        'float': {'initial': first_avail + addr_range * 2, 'count': 0},
        'char': {'initial': first_avail + addr_range * 3, 'count': 0}
    },
    'local': {
        'int': {'initial': first_avail + addr_range * 4, 'count': 0},
        'float': {'initial': first_avail + addr_range * 5, 'count': 0},
        'char': {'initial': first_avail + addr_range * 6, 'count': 0}
    },
    'temporal': {
        'int': {'initial': first_avail + addr_range * 7, 'count': 0},
        'float': {'initial': first_avail + addr_range * 8, 'count': 0},
        'char': {'initial': first_avail + addr_range * 9, 'count': 0},
        'bool': {'initial': first_avail + addr_range * 10, 'count': 0}
    },
    'constant': {
        'int': {'initial': first_avail + addr_range * 11, 'count': 0},
        'float': {'initial': first_avail + addr_range * 12, 'count': 0},
        'char': {'initial': first_avail + addr_range * 13, 'count': 0}
    }
}


def get_avail(scope, v_type):
    global virtual_memory
    assigned_addr = virtual_memory[scope][v_type]['initial'] + virtual_memory[scope][v_type]['count']  # initial + count
    virtual_memory[scope][v_type]['count'] += 1  # update count
    return assigned_addr


def get_count(scope, v_type):
    global virtual_memory
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


