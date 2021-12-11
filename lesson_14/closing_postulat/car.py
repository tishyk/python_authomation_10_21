class Car:
    def __init__(self, color: str, number_of_doors: int):
        self.__color = color  # _Car__color
        self._number_of_doors = number_of_doors
        self.number_of_wheels = 4

    def accelerate(self):
        print(self.__color)
        print("Car was accelaterated")

    def downgrade_speed(self):
        print("Car has downgrade speed")


class Toyota(Car):
    def move(self):
        print(self._number_of_doors)


if __name__ == '__main__':
    # car = Car("yellow", 4)
    # print(car._Car__color)
    # car.accelerate()
    # print(car._number_of_doors)
    toyota = Toyota("yellow", 4)
    toyota.move()
