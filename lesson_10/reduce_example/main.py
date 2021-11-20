from functools import reduce


number = [1, 2, 3, 4, 5, 6, 7, 8]


print(
    reduce(
        lambda a, b: a - b,
        number,
    )
)
