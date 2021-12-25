from lesson_20.functor.action import Action


class Human:
    def __init__(self, name: str, age: int, action: str) -> None:
        self.__name = name
        self.__age = age
        self.__action = Action(action)

    @property
    def action(self) -> str:
        return self.__action



if __name__ == "__main__":
    human = Human("John", 32, "dancing")
    print(human.action())