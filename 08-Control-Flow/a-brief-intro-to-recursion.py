#recursion is when a function calls itself

def count_down_from(number):
    if number <= 0:
        return 

    print(number)
    count_down_from(number - 1)

count_down_from(5)


def count_up_from(num):
    if num >=10:
        return 

    print(num)
    count_up_from(num + 1)

count_up_from(1)