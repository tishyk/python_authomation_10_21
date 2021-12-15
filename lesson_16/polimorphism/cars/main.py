from lesson_16.polimorphism.cars.dvs_car import DvsCar
from lesson_16.polimorphism.cars.electro_car import ElectroCar


if __name__ == "__main__":
    car_1 = DvsCar("Yellow", 1953)
    car_2 = ElectroCar("Silver", 2020)

    for car in [car_1, car_2]:
        car.turn_on_engine()