from typing import Type


class Column:
    def __init__(self, name: str, column_type: Type) -> None:
        self.__name = name
        self.__column_type = column_type
        self.__value = None

    def __set__(self, instance, value):
        self.__value = value

    def __get__(self, instance, owner):
        return self.__value
