'''Quickselect

Write a function that takes in an array of distinct integers as well as an integer k and that returns the kth smallest integer in that array.

The function should do this in linear time, on average.
'''

def quickselect(array, k):
    # Write your code here.
    return binaryPartition(array, k)

def binaryPartition(array, k):
    if k > len(array):
        return
    newArr = [0 for i in range(len(array)-1)]
    L = 0
    R = len(array)-2
    for i in range(1, len(array)):
        item = array[i]
        if item < array[0]:
            newArr[L] = item
            L += 1
        else:
            newArr[R] = item
            R -= 1
    print(array, newArr,array[0], L, k)
    if L > k-1:
        print('look left')
        return binaryPartition(newArr[:L], k)
    elif L < k-1:
        print('look right')
        return binaryPartition(newArr[L:], k-1-L)
    else:
        return array[0]

# sorted
# [(0, 2), (1, 3), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9)]

# [8, 5, 2, 9, 7, 6, 3]
# [5, 2, 7, 6, 3]
# [2, 3]
# 

# driver code
arr = [8, 5, 2, 9, 7, 6, 3]
k = 1

print(quickselect(arr, k))