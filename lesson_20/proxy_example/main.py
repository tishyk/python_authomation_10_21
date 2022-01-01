from lesson_21.proxy_example.disc import Disc


if __name__ == "__main__":
    disc = Disc("lesson_21/proxy_example/text.txt")
    disc.read()
    disc.read()
    disc.write("long string")
    disc.read()
