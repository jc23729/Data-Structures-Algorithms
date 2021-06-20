# Code walkthrough 
# Soliving in python 

##recursive binary search 

def binarySearch(array, target):
return binarySearchHelper(array, target, 0, array - 1)


def binarySearchHelper(array, target, left, right):
# base case is our right pointer greater than our left pointer
if left > right:
    return -1
middle = (left + right) // 2
# potental match number in arrray located in middle 
potentialMatch = array[middle]
if target === potentialMatch:
    # return our middle index
    return middle
elif target < potentialMatch:
    # were passing in middle -1 for our right pointer
    return binarySearchHelper(array, target, left, middle - 1)
else:
    return binarySearchHelper(array, target, middle +1 , right)