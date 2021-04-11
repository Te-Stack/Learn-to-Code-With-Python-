def accept_stuff(*args):
    print(type(args))
    print(args)

accept_stuff(1)
accept_stuff(1,3,5)
accept_stuff(1,2,3,4,5)

def my_max(non,*numbers):
    print(non)
    greatest = numbers[0]
    for number in numbers:
        if number >greatest:
            greatest = number
    return greatest            

print(my_max(1,2,3,4))