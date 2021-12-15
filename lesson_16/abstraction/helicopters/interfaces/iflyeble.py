from abc import ABC, abstractmethod


class IFlyable(ABC):
    @abstractmethod
    def come_up(self):
        ...

    @abstractmethod
    def land(self):
        ...
