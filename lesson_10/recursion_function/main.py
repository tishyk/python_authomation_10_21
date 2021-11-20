counter = 0

# while True:
#     if counter == 10:
#         break
#     print(counter)
#     counter += 1



def rec_example(counter: int):
    if counter == 10:
        return
    else:
        print(counter)
        counter += 1
        rec_example(counter)


rec_example(0)