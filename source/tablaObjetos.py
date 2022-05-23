tabla_obj = {}


def add_object(obj_id):
    if obj_id in tabla_obj:
        print("ERROR: class", obj_id, "already exists.")
        exit()

    else:
        tabla_obj[obj_id] = {'attributes': {}, 'methods': {}, 'parent': ''}


def add_attribute(obj_id, attr_id, attr_type):
    if attr_id not in tabla_obj[obj_id]['attributes']:
        tabla_obj[obj_id]['attributes'][attr_id] = attr_type


def add_method(obj_id, mthd_id, mthd_type):
    if mthd_id not in tabla_obj[obj_id]['methods']:
        tabla_obj[obj_id]['methods'][mthd_id] = mthd_type


def print_obj_table():
    for obj in tabla_obj:
        if tabla_obj[obj]['attributes']:
            print("\nAttributes for OBJECT", obj)
            for attr in tabla_obj[obj]['attributes']:
                print("ID:", attr, "\tType:", tabla_obj[obj]['attributes'][attr])
        if tabla_obj[obj]['methods']:
            print("\nMethods for OBJECT", obj)
            for mthd in tabla_obj[obj]['methods']:
                print("ID:", mthd, "\tType:", tabla_obj[obj]['methods'][mthd])
        print("---------------------------------------------------------------")


def validate_class(obj_id):
    if obj_id not in tabla_obj:
        print("ERROR: Parent class", obj_id, "was not defined.")
        exit()


def validate_attribute(obj_id, attr):
    if attr not in tabla_obj[obj_id]['attributes']:
        print("ERROR: Variable", attr, "is not an attribute of class", obj_id)
        exit()


def validate_method(obj_id, mthd):
    parent = tabla_obj[obj_id]['parent']
    if parent:
        if mthd not in tabla_obj[parent]['methods'] and mthd not in tabla_obj[obj_id]['methods']:
            print("ERROR: Function", mthd, "is not a method of class", obj_id, "nor its parent", parent)
            exit()
    elif mthd not in tabla_obj[obj_id]['methods']:
        print("ERROR: Function", mthd, "is not a method of class", obj_id)
        exit()


def assign_parent(child_id, parent_id):
    if child_id in tabla_obj:
        tabla_obj[child_id]['parent'] = parent_id
