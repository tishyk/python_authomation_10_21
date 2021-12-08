class Car:
    def __init__(self, color: str, number_of_wheels: int, type: str) -> None:
        self.__color = color
        self.__number_of_wheels = number_of_wheels
        self.__type = type

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        print("Hello from color method")
        self.__color = color


if __name__ == "__main__":
    toyota = Car("Yellow", 4, "Toyota")
