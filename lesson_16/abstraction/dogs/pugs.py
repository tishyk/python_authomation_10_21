from lesson_16.abstraction.dogs.dog import Dog


class Pug(Dog):
    def bark(self):
        print("Quite voice")

    def breathe(self):
        print("I am snoring")