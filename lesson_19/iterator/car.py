class Car:
    def __init__(self, model: str, color: str, number: str) -> None:
        self.__model = model
        self.__color = color
        self.__number = number

    def __modify_private_key(self, key: str) -> str:
        return key.replace(f"_{self.__class__.__name__}__", "")


    def __str__(self) -> str:
        start = "{\n"
        content = ""
        end = "}"

        for key, value in self.__dict__.items():
            content += f"\t{self.__modify_private_key(key)}: {value}\n"

        return f"{start}{content}{end}"