Quarterly_revenue = [15000,12511,12446,245424,286,248]
print(len(Quarterly_revenue))

Quarterly_revenue = [15000,12511,12446,245424,286,248, 567, 789, 234]
print(len(Quarterly_revenue))


Quarterly_revenue = [15000,12511,12446,245424,286,248]
#Initialising a variable and setting it value to 0
count = 0

#caling a for loop and iterating over each  integer in list 
for number in Quarterly_revenue:
    #then adding +1 over each value iterated over.
    count += 1
    #Setting a print function to print out the updated variable count 
print(count)

#Checking the type of the variable count to make sure it's an integer
print(type(count))