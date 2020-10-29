'''Max Subset Sum No Adjacent

Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array.

If a sum can't be generated, the function should return 0.
'''

def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return max(array[0], array[1])
    runningSum = float('inf')
    first = array[0]
    second = max(first, array[1])
    for i in range(2, len(array)):
        runningSum = max(second, first+array[i])
        first = second
        second = runningSum
    return runningSum


array = [75, 105, 120, 75, 90, 135]

print(maxSubsetSumNoAdjacent(array)) # True