'''Longest Peak

Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.


'''

# o(n) time | o(1) space
def longestPeak(array):
    # Write your code here.
    widest = [0, 0]
    for i in range(1, len(array)-1):
        left = i-1
        right = i+1
        if array[left] < array[i] > array[right]:
            # print(array[i])

            # expand to the left, within leftbound
            while left - 1 > -1 and array[left] > array[left-1]:
                left -= 1

            # expand to the right, within rightbound
            while right +1 < len(array) and array[right] > array[right+1]:
                right += 1

            # quick calculation of widest range    
            widest = max(widest, [left, right], key=lambda x: x[1] - x[0])
            
    print('wides range between indices: ', widest)
    return (widest[1]-widest[0])+1 if (widest[1]-widest[0]) else 0


array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

print(longestPeak(array)) # 6 --> 0, 10 ,6, 5, -1, 3