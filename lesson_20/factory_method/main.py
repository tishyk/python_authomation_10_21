from lesson_21.factory_method.cars.bmw import BMW
from lesson_21.factory_method.cars.toyota import Toyota
from lesson_21.factory_method.factory import CarFactory


if __name__ == "__main__":
    model = input("Enter name of model: (bmw / toyota)\n")
    car = CarFactory.get_car(model)
    print(car)
