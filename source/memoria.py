virtual_memory = {
    'global': {
        'int': 1000,
        'float': 2000,
        'char': 3000
    },
    'local': {
        'int': 4000,
        'float': 5000,
        'char': 6000
    },
    'temporal': {
        'int': 7000,
        'float': 8000,
        'char': 9000,
        'bool': 10000
    },
    'constant': {
        'int': 11000,
        'float': 12000,
        'char': 13000,
    }
}


def get_avail(scope, v_type):
    global virtual_memory
    assigned_addr = virtual_memory[scope][v_type]
    virtual_memory[scope][v_type] += 1
    next_addr = virtual_memory[scope][v_type]
    print("Assigned address:", assigned_addr)
    print("Next address:", next_addr, "\n")

# TODO : Function to reset addresses
# def reset_scope(scope):


while True:
    t_scope = input("Enter scope: ")
    t_type = input("Enter var type: ")
    get_avail(t_scope, t_type)
