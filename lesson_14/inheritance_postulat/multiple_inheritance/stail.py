class Reptile:
    def __init__(self):
        self.type = "Reptile"

    def swim(self):
        print("I am swimming...")


class Turtle(Reptile):
    def __init__(self):
        super().__init__()
        self.speed = "slow"

    def move(self):
        print("Super slow motion...")


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.move_type = "crawling"

    def move(self):
        print("Super fast motion...")


class Snail(Turtle, Snake):
    def __init__(self):
        super(Snail, self).__init__()
        super(Turtle, self).__init__()


if __name__ == '__main__':
    snail = Snail()
    snail.move()
