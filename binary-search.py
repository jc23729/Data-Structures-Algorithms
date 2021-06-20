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
		shiftAndUpdate(threeLargest, num, 2) 
	elif threeLargest(0) is None or num > threeLargest[0]:
		shiftAndUpdate(threeLargest, num, 0)
#so now we can pass an index, we just want to update our 3rd largest number
def shiftAndUpdate(array, num, idx):
	#if we passed an array of index of 2
	# [0, 1, 2] indecs
	# [x, y, z]
	# # for in range from 0 and 2 +1(1 is excluded of the range) (0, 2+ 1)
	# if i == 2: then we update this z to be our number which is 
	# we update index of 2 to be our num
	# [0, 1, 2]
	# [y, z, num]
	
	#index plus 1 is exclusive
	for i in range (idx + 1):
		#if i == idx. If were at the point were we are in our last index 
		if i == idx:
			#we want to update array of 1 to our number that we want to put
			array [1] = num
			#
		else:
			array [i] = array[i + 1]
		