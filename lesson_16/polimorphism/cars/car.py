from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, color: str, year: int) -> None:
        self._color = color
        self._year = year

    @abstractmethod
    def turn_on_engine(self):
        ...
