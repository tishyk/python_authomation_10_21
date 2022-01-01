class Action:
    def __init__(self, name: str) -> None:
        self.__name = name

    def __call__(self) -> str:
        return f"I am {self.__name}..."
    
    def do(self) -> str:
        return f"I am {self.__name}..."
