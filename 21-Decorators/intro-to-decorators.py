def be_nice(fn):
    def inner():
        print("Nice to meet you! i 'm honored to execute your function for you")
        fn()
        print("it was my pleasure executing your function! Have a nice day!")

    return inner


print("hi")
#@be_nice
def complex_business_logic():
    print("Something complex!")    

be_nice(complex_business_logic)()

#@be_nice
def another_fancy_function():
    print("Goo goo gaaaga")    



