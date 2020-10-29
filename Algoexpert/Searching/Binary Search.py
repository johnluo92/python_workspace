'''Binary Search

Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1

sample input = [0,1,21,33,45,45,61,71,72,73]
target: 33

sample output: 3'''

def binarySearch(array, target):
    # Write your code here.
    leftIdx = 0
    rightIdx = len(array)
    if len(array) == 0:
        return -1
    while leftIdx < rightIdx:
        mid = (leftIdx + rightIdx) // 2
        
        # checks if the target is found at this index location
        if target == array[mid]:
            return mid
        
        elif target < array[mid]:
            rightIdx = mid
        else:
            leftIdx = mid+1
    return -1

array = [0,1,21,33,45,45,61,71,72,73]
target = 33

print(binarySearch(array, target))