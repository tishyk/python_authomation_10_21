def set_number():
    number = 100

    def inner_function():
        nonlocal number
        number += 50
        print(number)
    
    inner_function()


set_number()
