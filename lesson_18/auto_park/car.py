class Car:
    def __init__(self, year: int, color: str, model: str) -> None:
        self.__year = year
        self.__color = color
        self.__model = model


    def __clean_private_key(self, key: str):
        return key.replace(f"_{self.__class__.__name__}__", "")


    def __str__(self) -> str:
        start = "{\n"
        content = ""
        end = "}"

        for key, value in self.__dict__.items():
            content += f"\t{self.__clean_private_key(key)}: {value}\n"

        return f"{start}{content}{end}"
