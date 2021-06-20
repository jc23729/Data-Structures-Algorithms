# Code walkthrough 
# Soliving in python 

##recursive binary search 



def binarySearch(array, target):
return binarySearchHelper(array, target, 0, array - 1)


def binarySearchHelper(array, target, left, right):
# base case is our right pointer greater than our left pointer
while left <= right:
    middle = (left + right) // 2
    # potental match number in arrray located in middle 
    potentialMatch = array[middle]
    if target === potentialMatch:
        # return our middle index
        return middle
    elif target < potentialMatch:
        right = middle -1
    else:
        left = middle + 1
return -1
        




# [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

def findThreeLargestNumbers(array):
    # Write your code here.
    threeLargest = [None, None, None]
	for num in array:
		updateLargest(threeLargest, num)
		return threeLargest

# so what we are checing one by one from the largest if these current numbers greater than our current numbers
	
def updateLargest(threeLargest, num):
# 	if threeLargest at index 2 is none, meaning we don't have a number there yet
#	or num our current number is greater than whats in index of 2
#	we want to update that current value 
	if threeLargest[2] is None or num > threeLargest[2]:
		shiftAndUpdate() #Todo
	#then if neither of these conditions are met, meaning we have a number here on the third value
	#then we want to compare to our second biggest number
	elif threeLargest[1] is None or num > threeLargest[1]:
		shiftAndUpdate() #TODO
	elif threeLargest(0) is None or num > threeLargest[0]:
		shiftAndUpdate()#