"""Bad example without polimorphism"""


class Employee:
    def __init__(self, position: str) -> None:
        self.__position = position

    def do_work(self):
        if self.__position == "developer":
            print("I am developing application")
        elif self.__position == "manager":
            print("I am working on falicitation of discussion and planning sprint")
        elif self.__position == "analyst":
            print("I am working on filtering input data from client and transformation into requirements")
        else: 
            raise Exception("Not supported position")
