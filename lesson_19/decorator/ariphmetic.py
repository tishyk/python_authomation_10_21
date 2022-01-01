class Power:
    def __init__(self, function: callable) -> None:
        self.__function = function

    def __call__(self, a: int, b: int) -> int:
        return self.__function(a, b) ** 2


@Power
def multiply(a, b):
    return a * b


if __name__ == "__main__":
    print(multiply(2, 2))