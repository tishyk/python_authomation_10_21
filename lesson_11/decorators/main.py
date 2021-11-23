from typing import Callable


def star(function: Callable):
    def decoratee():
        header = "*" * 10
        footer = "*" * 10

        return f"{header}\n{function()}\n{footer}"
    return decoratee


@star
def do_print():
    return "Hello world"



print(do_print())
