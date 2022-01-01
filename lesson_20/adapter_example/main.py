from typing import Counter, List

from lesson_21.adapter_example.employee import Employee


if __name__ == "__main__":
    my_employees: List[Employee] = []

    with open("lesson_21/adapter_example/employees.csv") as employees:
        counter = 0
        for employee in employees:
            if counter == 0:
                counter += 1
                continue

            my_employees.append(
                Employee.from_string(employee)
            )

    for item in my_employees:
        print(item.to_dict())