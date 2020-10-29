'''Subarray Sort

Write a function that takes in an array of at least two integers and that returns an array of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted (in ascending order)

If the input array is already sorted, the function should return [-1, -1]
'''

# o(nlog(n)) time | o(n) space
def subarraySort(array):
    # Write your code here.
    myList = list(enumerate(sorted(array)))
    print(myList)
    firstIndex = -1
    secondIndex = -1
    for i in range(len(array)):
        if array[i] != myList[i][1] and firstIndex == -1:
            firstIndex = i
        if array[i] != myList[i][1]:
            secondIndex = i
    return [firstIndex, secondIndex]

array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

print(subarraySort(array)) # [3,9]