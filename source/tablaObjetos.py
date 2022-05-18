tabla_obj = {}


def add_object(obj_id):
    if obj_id in tabla_obj:
        print("ERROR: class", obj_id, "already exists.")
        exit()

    else:
        tabla_obj[obj_id] = {}


def add_attribute(obj_id, attr_id, attr_type):
    tabla_obj[obj_id][attr_id] = [attr_type]


def print_obj_table():
    for obj in tabla_obj:
        if tabla_obj[obj] != {}:  # object has attributes
            print("\nAttributes for OBJECT", obj)
            for attr in tabla_obj[obj]:
                print("ID:", attr, "\tType:", tabla_obj[obj][attr][0])
            print("---------------------------------------------------------------")


def validate_parent(obj_id):
    if obj_id not in tabla_obj:
        print("ERROR: Parent class", obj_id, "was not defined.")
        exit()


def validate_attribute(obj_id, attr):
    if attr not in tabla_obj[obj_id]:
        print("ERROR: Variable", attr, "is not an attribute of class", obj_id)
        exit()
