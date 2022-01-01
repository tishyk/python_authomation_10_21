class Disc:
    def __init__(self, path: str) -> None:
        self.__path = path
        self.__is_actual = False
        self.__data = None

    def read(self) -> str:
        if self.__is_actual:
            return self.__data
        else:
            with open(self.__path) as file:
                self.__data = file.read()
                self.__is_actual = True
                
                return self.__data

    def write(self, text: str) -> None:
        with open(self.__path, "w") as file:
            file.write(text)
            self.__is_actual = False
