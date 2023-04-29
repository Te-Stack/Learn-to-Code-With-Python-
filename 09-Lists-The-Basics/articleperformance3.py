# Analysing the performance of each methods in executing 

#Importing time, length_hint and numpy module
import time
from operator import length_hint
import numpy as np

#Creating our list containing integers 
Quarterly_revenue = [15000,12511,12446,245424,286,248]


#Printing out the items in the list 
print('The items in the list are: ' + str(Quarterly_revenue))

# 1. Finding the length_list using the Naive method(For loop)


# Taking note of the start time 
begin_time_constraint = time.perf_counter()

# we will initialise the length as 0 and then use the for loop to get the list length
length = 0
for I in Quarterly_revenue:

   length = length + 1

#Taking note of the end time to know the time it took to execute
end_time_constraint = str(time.perf_counter() - begin_time_constraint)

# 2. Finding the length_list using the Built-in function len()

# Taking note of the start time 
begin_time_len = time.perf_counter()
#use the built in len() to get the list length
length_of_list = len(Quarterly_revenue)
#Taking note of the end time to know the time it took to execute
end_time_len = str(time.perf_counter() - begin_time_len)

# 3. Finding the length_list using the length_hint() method

# Taking note of the start time 
begin_time_hint = time.perf_counter()
#use the length_hint() method to get the list length
length_hint_list = length_hint(Quarterly_revenue)
#Taking note of the end time to know the time it took to execute
end_time_hint = str(time.perf_counter() - begin_time_hint)


#4. Finding the length_list using the numpy Module 

# Taking note of the start time 
begin_time_numpy = time.perf_counter()
#use the numpy module to get the list length
length_numpy_list = np.size(Quarterly_revenue)
#Taking note of the end time to know the time it took to execute
end_time_numpy = str(time.perf_counter() - begin_time_numpy)

#printing out all the results
print('The time taken by naive method to calculate the length of the list is: ' + end_time_constraint)
print('The time taken by len method to calculate the length of the list is: ' + end_time_len)
print('The time taken by length_hint method to calculate the length of the list is: ' + end_time_hint)
print('The time taken by numpy module method to calculate the length of the list is: ' + end_time_numpy)