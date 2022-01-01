from typing import Dict
from lesson_20.decorator.hobby import Hobby


@Hobby("dancing")
class Human:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def __modify_key(self, key: str) -> str:
        return key.replace(f"_{self.__class__.__name__}__", "")

    def json(self) -> Dict[str, str]:
        data = {}

        for key, value in self.__dict__.items():
            data[self.__modify_key(key)] = value
        
        return data

if __name__ == "__main__":
    john = Human("John", 32)
    print(john.hobby)