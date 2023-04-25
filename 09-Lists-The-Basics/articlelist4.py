#importing numpy as np you can import it as anything but this is just the conventional way
import numpy as np

#The list containing different range of integers 
Quarterly_revenue = [15000,12511,12446,245424,286,248]

# getting list length using the __len__() method and storing it inside a variable
length_list = np.size(Quarterly_revenue)


print(length_list)