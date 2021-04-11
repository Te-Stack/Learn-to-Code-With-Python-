import functools

def be_nice(fn):
    @functools.wraps(fn)
    def inner(*args,**kwargs):
        print("Nice to meet you! i 'm honored to execute your function for you")
        result = fn(*args,**kwargs)
        print("it was my pleasure executing your function! Have a nice day!")
        return result

    return inner


@be_nice
def complex_business_sum(a,b):
    "Adds two numbers together"
    return a + b


help(complex_business_sum)    