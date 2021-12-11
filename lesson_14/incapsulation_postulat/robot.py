from enum import Enum
from typing import Tuple


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    BACK = 2
    FORWARD = 3


class Robot:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def move(self, direction: Direction, distance: int):
        if direction == Direction.RIGHT:
            self.__x += distance
        elif direction == Direction.LEFT:
            self.__x -= distance
        elif direction == Direction.BACK:
            self.__y -= distance
        elif direction == Direction.FORWARD:
            self.__y += distance
        else:
            raise Exception("Not supported direction...")

    @property
    def position(self) -> Tuple[int, int]:
        return self.__x, self.__y


if __name__ == '__main__':
    robot = Robot()
    print(robot.position)
    robot.move(Direction.FORWARD, 50)
    robot.move(Direction.LEFT, 20)
    print(robot.position)
