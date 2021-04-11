# A programming pattern in which a scope is retains access to an enclosing scope's name

def outer():
    candy = "Snickers"

    def inner():
        return candy

    return inner 


the_func = outer()
print(the_func)    
