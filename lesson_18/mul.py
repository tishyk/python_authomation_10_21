class Mul:
    def __init__(self, speed: int, strength: int) -> None:
        self.__speed = speed
        self.__strength = strength

    def __str__(self) -> str:
        result = ""

        for key, value in self.__dict__.items():
            result += f"{key} => {value}\n"
        
        return result