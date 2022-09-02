


#Finding the smallest number in an array 
def findSmallest(arr):
    smallest = arr[0] #Stores the smallest value 
    smallest_index = 0 #Stores the index of the value
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index



def findBiggest(arr):
    biggest = arr[0]
    biggest_index = 0
    for i in range(1,len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_index = i
    return biggest_index

def selectionSortBig(arr):
    newArr = []
    for i in range(len(arr)):
        biggest = findBiggest(arr)
        newArr.append(arr.pop(biggest))
    return newArr

#Sorting Algorithms 
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,3,6,2,10]))
print(selectionSortBig([5,3,6,2,10]))


        
        

