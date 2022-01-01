from __future__ import annotations
from typing import Dict


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        salary: int,
    ) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__salary = salary

    def __str__(self) -> str:
        return f"{self.__first_name} {self.__last_name}"

    @classmethod
    def from_string(cls, csv_line: str) -> Employee:
        items = csv_line.split(',')
        
        return cls(*items)

    def to_dict(self) -> dict:
        data = {}

        for key, value in self.__dict__.items():
            data[key] = value

        return data
