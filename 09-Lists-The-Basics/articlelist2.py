#To use the length_hint function it has to be imported from the operator module.
from operator import length_hint

#The list we intend  to find its length 
Quarterly_revenue = [15000,12511,12446,245424,286,248]

#Checking the type of the variable count to make sure it's an integer
print(length_hint(Quarterly_revenue))
#Output: 6

