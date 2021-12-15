from lesson_16.employees.employees.buisness_analyst import BusinessAnalyst
from lesson_16.employees.employees.developer import Developer
from lesson_16.employees.employees.manager import Manager


if __name__ == "__main__":
    analytics = BusinessAnalyst("John", "Dow", 1234567, 23, 2, 15)
    deleloper = Developer("James", "Smith", 98776554, 23, 1, 4)
    manager = Manager("Bob", "Barateon", 98909887, 40, 4, 20)

    print(analytics.do_work())
    print(deleloper.do_work())
    print(manager.do_work())
