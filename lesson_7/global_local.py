# global scope
name = "John"

def change_name(outer_name):
    # local scope
    inner_name = "Marta"

    return outer_name + inner_name



def do_someting():
    global name
    name = "Marta"
    print(name)


do_someting()
print(name)