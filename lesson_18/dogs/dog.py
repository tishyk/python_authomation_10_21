class Dog:
#     def __new__(cls):
#         print(f"{cls.__name__} was born...")

#         return super().__new__(cls)
    
#     def __del__(self):
#         print(f"{self.__class__.__name__} is dead...")

    def __init__(self, name: str, breed: str) -> None:
        self.__is_alive = True
        self.__name = name
        self.__breed = breed

    def change_status(self):
        self.__is_alive = not self.__is_alive

    # def __bool__(self):
    #     return self.__is_alive

    # def __getattr__(self, item: str):
    #     return "Default"
    
    # def __getattribute__(self, name: str):
    #     return super().__getattribute__(name)

    # def update_status(self):
    #     self.__is_alive = not self.__is_alive

    def __setattr__(self, __name: str, __value) -> None:
        self.__dict__[__name] = __value


if __name__ == "__main__":
    dog = Dog("John", "Buldog")

    # dog.update_status()


    dog._Dog__name = "James"




    # dog.change_status()
    # print(dog.name)

    # dog.change_status()

    # if dog:
    #     print("Dog is alive")
    # else: 
    #     print("Dog is dead")
