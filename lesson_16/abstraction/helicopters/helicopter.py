from lesson_16.abstraction.helicopters.interfaces.iflyeble import IFlyable
from lesson_16.abstraction.helicopters.interfaces.irotorable import IRotorable


class Helicopter(IFlyable, IRotorable):
    def __init__(self) -> None:
        self.__main_rotor = False
        self.__second_rotor = False
        self.__is_on_earth = True
        self.__is_engine_on = False

    def come_up(self):
        self.__is_engine_on = True
        self.rotate()
        self.__is_on_earth = False

    def rotate(self):
        self.__main_rotor = True
        self.__second_rotor = True
