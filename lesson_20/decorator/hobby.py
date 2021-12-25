from typing import Type


class Hobby:
    def __init__(self, name: str) -> None:
        self.__name = name
    
    def __call__(self, _type: Type) -> Type:
        setattr(_type, f"_{_type.__name__}__hobby", self.__name)
        return _type
