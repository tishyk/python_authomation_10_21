# static function
# def print_name(name: str) -> str:
#     return f"Hello {name}"


# lambda function with name invocation
print_name = lambda fist_name, last_name: f"Hello {fist_name} {last_name}"
print(print_name("Marta", "Smith"))


# lambda function invocation
# print(
#     (lambda name: f"Hello {name}")("John")
# )
