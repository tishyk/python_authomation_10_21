def say_hello(*args):
    for name in args:
        print(f"Hello {name}")


# say_hello("John", "Marta", "Jane", "Jason", "Alex")



def set_premiya(**kwargs):
    kwargs["salary"] = 10000

    return kwargs


john = {"name": "John", "age": 32, "gender": "male", "salary": 5000}

new_john = set_premiya(**john)
print(new_john)
