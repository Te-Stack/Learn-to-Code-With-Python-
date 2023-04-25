# here, we will analyse the performance of our code
# to find the length of the list

# we are importing the length_hint function
import timeit
import time
from operator import length_hint

# now, we will initialise our list with items in it

list_of_items = [1, 3, 5, 7, 9, 11]

# first, we will print the list of items as it is

print('The items in the list are: ' + str(list_of_items))

# now, we will find the length of the list
# we will initialise the length as 0

begin_time_constraint = time.perf_counter()
print(begin_time_constraint)


length = 0
for I in list_of_items:

   length = length + 1

end_time_constraint = str(time.perf_counter() - begin_time_constraint)
print(end_time_constraint)
