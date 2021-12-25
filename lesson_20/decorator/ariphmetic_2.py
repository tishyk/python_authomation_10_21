from typing import Callable


class Power:
    def __init__(self, pow: int) -> None:
        self.__pow = pow

    def __call__(self, function: Callable) -> Callable:
        def inner(a: int, b: int) -> int:
            return function(a, b) ** self.__pow
        return inner


@Power(3)
def multiply(a, b):
    return a * b


if __name__ == "__main__":
    print(multiply(2, 2))