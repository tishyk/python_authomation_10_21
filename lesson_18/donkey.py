class Donkey:
    def __init__(self, name: str, color: str) -> None:
        self.__speed = 5
        self.__strength = 10
        self.__name = name
        self.__color = color
    
    def __str__(self) -> str:
        result = ""

        for key, value in self.__dict__.items():
            result += f"{key} => {value}\n"
        
        return result

    @property
    def strength(self):
        return self.__strength
