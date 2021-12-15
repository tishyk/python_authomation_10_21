from lesson_16.polimorphism.cars.car import Car


class DvsCar(Car):
    def __init__(self, color: str, year: int) -> None:
        super().__init__(color, year)
        self.__engine = False

    def turn_on_engine(self):
        self.__engine = True
        print("Single engine is turned on")