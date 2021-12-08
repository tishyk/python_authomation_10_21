class House:
    def __init__(
        self,
        stages: int,
        windows: int,
        address: str,
        style: str,
        walls: int,
        square: int,
        doors: int,
        rooms: int,
    ) -> None:
        self.__stages = stages
        self.__windows = windows
        self.__address = address
        self.__style = style
        self.__walls = walls
        self.__square = square
        self.__doors = doors
        self.__rooms = rooms


    def add_stage(self):
        self.__stages += 1

    @property
    def electro_bill(self) -> float:
        return self.__rooms * 15

    @property
    def square(self) -> float:
        return self.__square

    @property
    def stages(self):
        return self.__stages


if __name__ == "__main__":
    house = House(
        stages=2,
        windows=10,
        address="Backer street 32",
        style="modern",
        walls=10,
        square=120,
        doors=10,
        rooms=6,
    )

    print(house.electro_bill)
    # print(house.rooms)
    print(house.square)
    house.add_stage()
    print(house.stages)
