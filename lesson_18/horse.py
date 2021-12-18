from lesson_18.donkey import Donkey
from lesson_18.mul import Mul


class Horse:
    def __init__(self, name: str, model: str) -> None:
        self.__speed = 10
        self.__strength = 5
        self.__name = name
        self.__model = model

    def __str__(self) -> str:
        result = ""

        for key, value in self.__dict__.items():
            result += f"{key} => {value}\n"
        
        return result

    def __add__(self, other: Donkey):
        return Mul(self.__speed, other.strength)

    def __radd__(self, other: Donkey):
        return Mul(self.__speed, other.strength)

    @property
    def speed(self):
        return self.__speed
