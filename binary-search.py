# Code walkthrough 
# Soliving in python 
def binarySearch(array, target):
return binarySearchHelper(array, target, 0, array - 1)


def binarySearchHelper(array, target, left, right):
# base case is our right pointer greater than our left pointer.