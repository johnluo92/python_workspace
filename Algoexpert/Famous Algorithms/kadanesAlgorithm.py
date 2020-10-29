'''Kadane's Algorithm

Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by sunmming up all of the integers in a non-empty subarray of the input array.

A subarray must only contain adjacent numbers.
'''
def kadanesAlgorithm(array):
# Write your code here.
    runningSum = array[0]
    maxSoFar = array[0]
    i = 1
    while i <= len(array)-1:
    	# iterate through array
    	# remember current max to be the current runningSum or the number at the index of the array. If a previous number say is infinitely smaller, pulling down the sum of the previous integer sums, then it would be best to see if the current number is greater than the sum you just calculated.
        runningSum = max(array[i], runningSum+array[i])
        maxSoFar = max(maxSoFar, runningSum)
        print('currentNum {} | runningSum: {} | maxSoFar {}'.format(array[i], runningSum, maxSoFar))
        i += 1
    return maxSoFar



arr = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanesAlgorithm(arr))