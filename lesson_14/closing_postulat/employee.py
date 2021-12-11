class Employee:
    def __init__(self, name: str, salary: int, position: str):
        self._name = name
        self._salary = salary
        self._position = position

    def do_work(self):
        print("I am working...")


class Director(Employee):
    def __init__(self, name, salary, department: str):
        super().__init__(name, salary, position="director")
        self.__department = department


class Worker(Employee):
    def __init__(self, name, salary, director: Director):
        super().__init__(name, salary, position="worker")
        self.__director = director


if __name__ == '__main__':
    director = Director("James", 5000, "IT")
    worker = Worker("John", 1500, director)
    print()
