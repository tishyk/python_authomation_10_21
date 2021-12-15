from lesson_16.polimorphism.cars.car import Car


class ElectroCar(Car):
    def __init__(self, color: str, year: int) -> None:
        super().__init__(color, year)
        self.__forward_right_engine = False
        self.__forward_left_engine = False
        self.__back_right_engine = False
        self.__back_left_engine = False
        
    def turn_on_engine(self):
        self.__forward_right_engine = True
        self.__forward_left_engine = True
        self.__back_right_engine = True
        self.__back_left_engine = True
        print("All engines are turned on")
        