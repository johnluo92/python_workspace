'''Smallest Difference

Write a function that takes in two non-empty arrays of integers, finds the pair of the numbers (one from each array) whose absolute diference is colest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.'''

# o(nlog(n)) + o(mlog(m)) time | o(1) space
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    ans = [float('inf'), float('-inf')]
    arr1, arr2 = sorted(arrayOne), sorted(arrayTwo)
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if abs(arr1[i] - arr2[j]) == 0:
            return [arr1[i], arr2[j]]
        ans = min(ans, [arr1[i],arr2[j]], key=lambda x: abs(x[0] - x[1]))
        if arr1[i] > arr2[j]:
            j += 1
        else:
            i += 1
            
    return ans

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

print(smallestDifference(arrayOne,arrayTwo)) # [28, 26]