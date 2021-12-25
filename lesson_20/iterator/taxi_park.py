from typing import List
from lesson_20.iterator.car import Car


class TaxiPark:
    def __init__(self, cars: List[Car] = None) -> None:
        self.__cars = [] if not cars else cars
        self.__current = 0

    def add_car(self, car: Car) -> None:
        self.__cars.append(car)

    def add_cars(self, cars: List[Car]) -> None:
        self.__cars.extend(cars)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current < len(self.__cars):
            car = self.__cars[self.__current]
            self.__current += 1
            return car
        else: 
            raise StopIteration
