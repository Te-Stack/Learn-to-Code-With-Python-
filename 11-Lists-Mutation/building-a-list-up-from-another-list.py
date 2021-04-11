powerballs_numbers = [4,8,15,16,23,42]

def squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    return squares 

print(squares(powerballs_numbers)) 

def convert_to_floats(numbers):
    floats = []
    for number in numbers:
        floats.append(float(number))
    return floats  

print(convert_to_floats(powerballs_numbers)) 

def even_or_odd(numbers):
    result = []
    for number in numbers:
        if number % 2 ==0:
            result.append(True)
        else:
            result.append(False)
    return result

print(even_or_odd(powerballs_numbers))    
