def update_employee(name: str, /, *, age: int, salary: int):
    pass


# update_employee("John", 32, 15000)  # ok
# update_employee(name="John", 32, 15000)  # ok

update_employee("John", age=32, salary=15000)
