from lesson_21.factory_method.cars.bmw import BMW
from lesson_21.factory_method.cars.car import Car
from lesson_21.factory_method.cars.toyota import Toyota


class CarFactory:
    @staticmethod
    def get_car(model: str) -> Car:
        """Return car according ato provided name."""

        if model == "toyota":
            return Toyota()
        elif model == "bmw":
            return BMW()
        else:
            raise Exception("Invalid car model.")
