class Human:
    
    children = ["Alex", "Maria"]

    def __init__(self, name: str, age: int, salary: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def get_name(self, name: str) -> str:
        return self.name

    def increment_age(self):
        self.age += 1

    def update_salary(self, salary: int):
        self.increment_age()

    @classmethod
    def create_one(cls, name: str, age: int, salary: int, gender: str):
        return cls(name, age, salary, gender)

    @classmethod
    def get_children(cls):
        return cls.children

    @staticmethod
    def calculate_premia(salary: int):
        return salary + 100

    def get_me(self) -> int:
        return self

    @classmethod
    def get_some(cls):
        return cls

if __name__ == "__main__":
    # john_1 = Human("john", 23, 1500, "male")
    # john_2 = Human("john", 23, 1500, "male")

    # print(id(john_1))
    # print(id(john_2))

    # john = Human.create_one("john", 23, 1500, "male")
    # print(john.name)

    john = Human("john", 23, 1500, "male")
    # marta = Human("marta", 32, 1500, "female")

    # print(john.children)
    # print(marta.children)

    # john.children.append("SOme")

    # print(john.children)
    # print(marta.children)

    # john.update_salary(2500)
    # print(john.age)

    # marta = john.create_one("Marta", 32, 1500, "female")
    # Human.get_name()  # error
    # print(Human.get_children())


    # print(Human.calculate_premia(500))

    # print(john.get_me())
    # print(Human.get_some())
