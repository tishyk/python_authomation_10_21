from typing import Dict
from lesson_18.auto_park.car import Car


class AutoPark:
    def __init__(self) -> None:
        self.__cars: Dict[Car] = {}
    
    def __setitem__(self, parking_number: int, item: Car):
        self.__cars[parking_number] = item

    def __getitem__(self, parking_number: int):
        return self.__cars[parking_number]