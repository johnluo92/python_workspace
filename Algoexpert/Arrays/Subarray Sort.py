'''Subarray Sort

Write a function that takes in an array of at least two integers and that returns an array of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted (in ascending order)

If the input array is already sorted, the function should return [-1, -1]
'''

# o(nlog(n)) time | o(n) space
# def subarraySort(array):
#     # Write your code here.
#     myList = list(enumerate(sorted(array)))
#     print(myList)
#     firstIndex = -1
#     secondIndex = -1
#     for i in range(len(array)):
#         if array[i] != myList[i][1] and firstIndex == -1:
#             firstIndex = i
#         if array[i] != myList[i][1]:
#             secondIndex = i
#     return [firstIndex, secondIndex]

# array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

# print(subarraySort(array)) # [3,9]

# ------------------------------------------------------

def subarraySort(array):
    # Write your code here.
    min_num, max_num = float('inf'), float('-inf')
    fix_left, fix_right = -1, -1

    # arr = [1, 2, 4, 7, 10,   11, 7, 12, 6,   7, 16, 18, 19]
    
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, array, num):
            print('TRUE')
            min_num = min(min_num, num)
            max_num = max(max_num, num)
            
    print(min_num, max_num)
    if min_num != float('inf'):
        fix_left = getLeftIdx(min_num, array)
        fix_right = getRightIdx(max_num, array)

    print([fix_left, fix_right])

def isOutOfOrder(i, array, num):
    if i == 0:
        return num > array[i+1]
    if i == len(array)-1:
        return array[i-1] > num
    return array[i-1] > num or num > array[i+1]
    
def getLeftIdx(min_num, array):
    for i in range(len(array)):
        if min_num < array[i]:
            return i
        
def getRightIdx(max_num, array):
    for i in reversed(range(len(array))):
        if max_num > array[i]:
            return i


arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
# arr = [2, 1]
# arr = [1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19] #4/9

subarraySort(arr)