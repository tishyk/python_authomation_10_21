from abc import ABC, abstractmethod


class Dog(ABC):
    def __init__(self, name: str, color: str) -> None:
        self._name = name
        self._color = color

    def bark(self):
        raise Exception(f"Method {self.bark.__name__} not implemented in {self.__class__.__name__}")

    def breathe(self):
        raise Exception(f"Method {self.breathe.__name__} not implemented in {self.__class__.__name__}")

    def eat(self):
        print("I am eating")
