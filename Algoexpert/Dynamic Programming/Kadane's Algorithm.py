'''Kadane's Algorithm

Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by summing up all of the integers in a non-empty subarray of the input array. A subarray must only contain adjacent numbers.
'''

def kadanesAlgorithm(array):
    # Write your code here.
	anotherArray = [None for i in array]
	runningSum = 0
	for i in range(len(array)):
		curNum = array[i]
		runningSum += curNum
		anotherArray[i] = max(curNum, runningSum)
		runningSum = anotherArray[i]
	# print(anotherArray)
	return max(anotherArray)

array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

print(kadanesAlgorithm(array)) # True
