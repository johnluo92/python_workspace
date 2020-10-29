'''Find Three Largest Numbers

Write a function that takes in an array of at least three integers and, without sorting the input array, returns a sorted array of the three largest integers in the input array.'''

def findThreeLargestNumbers(array):
    # Write your code here.
    return setHighestThree(array)

def setHighestThree(array):
    result = [None]*3
    result[2] = array[0]
    for i in range(1, len(array)):
        resHigh = result[2]
        
        if array[i] >= resHigh:
            result = setHighest(result, array[i])
        elif not result[1]:
            result[1] = array[i]
        elif array[i] >= result[1]:
            result[0] = result[1]
            result[1] = array[i]
        elif not result[0] and result[1]:
            result[0] = array[i]
        elif array[i] >= result[1]:
            prevMid = result[1]
            result[1] = array[i]
            result[0] = prevMid
        elif array[i] > result[0]:
            result[0] = array[i]
    
    return result
    
def setHighest(result, high):
    prevHigh, prevMid = result[2], result[1]
    result[2] = high
    result[1] = prevHigh
    result[0] = prevMid
    
    return result

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

print(findThreeLargestNumbers(array))