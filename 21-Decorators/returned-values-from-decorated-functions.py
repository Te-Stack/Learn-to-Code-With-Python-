def be_nice(fn):
    def inner(*args,**kwargs):
        print("Nice to meet you! i 'm honored to execute your function for you")
        result = fn(*args,**kwargs)
        print("it was my pleasure executing your function! Have a nice day!")
        return result

    return inner


@be_nice
def complex_business_logic(a,b):
    return a +  b


print(complex_business_logic(3,5))       
