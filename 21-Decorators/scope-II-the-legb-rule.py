# LEGB == Local/Enclosing Function / Global / Built- in
#x = 20

def outer():
    #x = 10

    def inner():
        #x = 4 
        return len

    return inner()


print(outer()("python"))    
