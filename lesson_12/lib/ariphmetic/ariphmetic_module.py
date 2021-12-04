from typing import Union
from .operations import (
    SUM,
    DIFFERENCE
)


def do_action(operation: str, arg1: int, arg2: int) -> Union[int, float]:
    if operation == SUM:
        return arg1 + arg2
    elif operation == DIFFERENCE:
        return arg1 - arg2
    else:
        pass
