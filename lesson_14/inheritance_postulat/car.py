class Car:
    def __init__(self, number_of_doors: int, color: str) -> None:
        self.__number_of_wheels = 4
        self.__number_of_doors = number_of_doors
        self.__color = color

    def __init_subclass__(cls, number_of_doors: int, color: str) -> None:
        super().__init_subclass__()

    def accelerate(self):
        print("Car was accelaterated")

    def downgrade_speed(self):
        print("Car has downgrade speed")


if __name__ == '__main__':
    car = Car(4, "yellow")
    car.accelerate()
    # car = Car(2, "Red")
