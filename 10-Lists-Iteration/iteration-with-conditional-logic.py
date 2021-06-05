values = [3,6,9,12,15,18,21,24]
other_values = [5,10,15,20,25,30]


def odds_sum(numbers):
    total = 0
    for number in numbers:  
        if number % 2 == 1:
            total += number 
    return total 


print(odds_sum(values))     
print(odds_sum(other_values)) 

  
   
def greatest_number(numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest= number     
    return greatest

print(greatest_number([1,10,3,4,5]))  


  


    