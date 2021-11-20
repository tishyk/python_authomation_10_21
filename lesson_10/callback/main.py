from typing import Callable, Union


def do_action(argument_1: int, argument_2: int, callback: Callable) -> Union[int, float]:
    return callback(argument_1, argument_2)


def do_division(argument_1: int, argument_2: int) -> float:
    return argument_1 / argument_2


def do_multiplication(argument_1: int, argument_2: int) -> int:
    return argument_1 * argument_2


def do_sum(argument_1: int, argument_2: int) -> int:
    return argument_1 + argument_2



print(do_action(5, 5, do_sum))
print(do_action(5, 5, do_division))
print(do_action(5, 5, do_multiplication))

