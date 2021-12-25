class Phone:
    def __init__(self, model: str, system: str) -> None:
        self.__model = model
        self.__system = system

    def __call__(self, number: str) -> None:
        print(f"I am calling {number} number...")
    

if __name__ == "__main__":
    phone = Phone("T10", "Android")
    phone("+380660213302")
