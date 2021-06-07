dinner = "Steak and Potatoes"

#for character in dinner:
#    print(character)

numbers = [2,4,6,8,10]

for value in numbers:
    print(value * value)

novelists = ["jim","tommy","aurthur"]

for novelist in novelists:
    print(len(novelist))

print(value)    
print(novelist)

total = 0

for value in numbers:
    total = total + value

print(total)    
print()

def iterTest(low,high):
    while low<=high:
        print(low)
        low=low+1
    

iterTest(1,10)
