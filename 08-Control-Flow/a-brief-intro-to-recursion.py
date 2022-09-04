#recursion is when a function calls itself

def count_down_from(number):
    print(number)
    if number <= 0:
        return 

    
    count_down_from(number - 1)

count_down_from(5)
print()

def count_up_from(num):
    print(num)
    if num >=10:
        return 

  
    count_up_from(num + 1)

count_up_from(1)
print()


def recurTest(low,high):
    if low<=high:
        print(low)
        recurTest(low+1,high)

recurTest(1,5)