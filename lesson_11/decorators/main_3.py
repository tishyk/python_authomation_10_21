from typing import Callable


def header_footer(sign: str):
    def foo(function: Callable):
        def decoratee(message: str):
            header = sign * 10
            footer = sign * 10

            return f"{header}\n{function(message)}\n{footer}"
        return decoratee
    return foo


@header_footer("^")
def do_print(message: str):
    return message


print(do_print("Hi all"))
