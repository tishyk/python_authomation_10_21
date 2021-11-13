def do_something():
    name = "John"

    def inner():
        print(name)
    
    return inner


function = do_something()
function()
