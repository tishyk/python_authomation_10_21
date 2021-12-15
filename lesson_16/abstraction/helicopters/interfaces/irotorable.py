from abc import ABC, abstractmethod


class IRotorable(ABC):
    @abstractmethod
    def rotate(self):
        ...
