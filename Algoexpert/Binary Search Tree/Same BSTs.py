'''Same BSTs

An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each integer in the array, from left to right, into the BST.

Write a function that takes in two arrays of integers and determines whether these arrays represent the same BST.
'''

def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if len(arrayOne) == 0 or len(arrayTwo) == 0:
    	return True
    if arrayOne[0] != arrayTwo[0]:
    	return False
    if len(arrayOne) != len(arrayTwo):
    	return False

    print(arrayOne, arrayTwo)

    smallOne = validateSmaller(arrayOne)
    smallTwo = validateSmaller(arrayOne)

    biggerOne = validateBigger(arrayTwo)
    biggerTwo = validateBigger(arrayTwo)

    return sameBsts(smallOne, smallTwo) and sameBsts(biggerOne, biggerTwo)

def validateSmaller(array):
	arrayToValidate = []
	for i in range(1, len(array)):
		if array[i] < array[0]:
			arrayToValidate.append(array[i])
	return arrayToValidate

def validateBigger(array):
	arrayToValidate = []
	for i in range(1, len(array)):
		if array[i] >= array[0]:
			arrayToValidate.append(array[i])
	return arrayToValidate



arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]

# small1: 8, 5, 2
# small2: 8, 5, 2

# big1: 15, 12, 94, 81, 11
# big2: 15, 12, 11, 94, 81

print(sameBsts(arrayOne, arrayTwo)) # True