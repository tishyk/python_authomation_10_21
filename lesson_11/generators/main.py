import sys

def squere_item(length: int):
    counter = 0

    while counter < length:
        yield counter
        counter += 1


numbers = list(range(1000000))

generator = squere_item(1000000)


print(sys.getsizeof(numbers))
print(sys.getsizeof(generator))

