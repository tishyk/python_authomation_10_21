from .employee import Employee


class Developer(Employee):
    def __init__(self, first_name: str, last_name: str, inn: int, age: int, experience: int, rate: int) -> None:
        super().__init__(first_name, last_name, inn, age, experience, rate)
        self.__area = "Software development"

    def do_work(self):
        super().do_work()
        print("I am developing application")
