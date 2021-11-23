def header_footer(sign: str):
    def foo(function):
        def decoratee():
            header = sign * 10
            footer = sign * 10

            return f"{header}\n{function()}\n{footer}"
        return decoratee
    return foo


@header_footer("#")
@header_footer("*")
def do_print():
    return "Hello world"


print(do_print())
