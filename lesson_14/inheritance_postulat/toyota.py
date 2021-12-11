from lesson_14.inheritance_postulat.car import Car


class Toyota(Car):
    def __init__(self, color: str, number_of_doors: int, model: str) -> None:
        super().__init__(number_of_doors, color)
        self.__model = model

    def accelerate(self):
        super().accelerate()
        print("Lets go")


if __name__ == "__main__":
    toyota = Toyota("yellow", 4, "XL")
    toyota.accelerate()
