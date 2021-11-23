def squere_item(length: int):
    counter = 0

    while counter < length:
        yield counter
        yield counter ** 2
        yield counter ** 3
        counter += 1


generator = squere_item(10)

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# for counter in generator:
#     print(counter)