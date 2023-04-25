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

begin_time_constraint = timeit.default_timer
print(begin_time_constraint)


length = 0
for I in list_of_items:

   length = length + 1

end_time_constraint = str(time.time() - begin_time_constraint)
print(end_time_constraint)

# we will find the length of the list using the len method below

begin_time_len = time.time()
length_of_list = len(list_of_items)
end_time_len = str(time.time() - begin_time_len)

# we will also find the length of the list using the lenth_hint method
# to find the time constraint of it

begin_time_hint = time.time()
length_hint_list = length_hint(list_of_items)
end_time_hint = str(time.time() - begin_time_hint)

# now, we will print all the results

print('The time taken by naïve method to calculate the length of the list is: ' + end_time_constraint)
print('The time taken by len method to calculate the length of the list is: ' + end_time_len)
print('The time taken by length_hint method to calculate the length of the list is: ' + end_time_hint)