john = {
    "name": "John",
    "age": 23,
    "salary": 12500,
    "gender": "male"
}

marta = {
    "name": "Marta",
    "age": 32,
    "salary": 2500,
    "gender": "female"
}


def get_name(person: dict) -> str:
    return person["name"]


def update_salary(person: dict, salary: int):
    person["salary"] = salary
