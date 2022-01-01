from typing import Type


def singleton(_type: Type):
    def decoratee(host: str, port: int):
        if hasattr(_type, "_instance"):
            return getattr(_type, "_instance")
        else:
            instance = _type(host, port)
            setattr(_type, "_instance", instance)
            return getattr(_type, "_instance")
    return decoratee
