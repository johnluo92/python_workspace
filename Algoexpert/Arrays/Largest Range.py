'''Largest Range

Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of integers contained in that array.

The first number in the output array should be the first number in the range, while the second number should be the last number in the range.

A range of numbers is defined as a set of numbers that come right after each other in the set of real integers. For instance, the output array [2,6] represents the range {2,3,4,5,6}. which is a range of length 5. Note that numbers don't need to be sorted or adjacent in the input array in order to form a range.
'''

# solution 1
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

def largestRange(array):
    visited = {num:False for num in array}
    longest = [0,0]
    for num in array:

        smaller, bigger = num-1, num+1
        while smaller in visited and not visited[smaller]:
            visited[smaller] = True
            smaller -= 1
        smaller += 1
        while bigger in visited and not visited[bigger]:
            visited[bigger] = True
            bigger += 1
        bigger -= 1

        longest = max(longest, [smaller, bigger], key = lambda x: x[1] - x[0])

    return longest

def largestRange(array):
    array = sorted(array)
    beg = end = array[0]
    
    if len(array) == 1:
        return [beg, end]
    
    length = len(array)
    result = [beg, end]
    
    for i in range(1, length):
        curresult = result[1]-result[0]
        test = end - beg
        if array[i] == array[i-1]+1:
            end = array[i]
            continue
        elif array[i] == array[i-1]:
            end = array[i]
            continue
        else:
            if curresult < end-beg:
                result[1] = end
                beg = array[i]
            elif curresult == end-beg:
                result[0] = result[1] = array[i]
                beg = end = array[i]

            
    if result[1]-result[0] < end-beg:
        result[0] = beg
        result[1] = end
    return result

array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

# ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(largestRange(array))
# ---------------------------------------------------------

# Solution 2

# o(n) time | o(n) space
def largestRange(array):
    '''
    using a hashtable solution to put all the values in it
    going through each value until all hash values of the
    list (which are now keys) are turned to True. We record this
    value and see if the next test's range is bigger than the 
    current range. We stop the loop/lookup for each array item
    when the full hashtable is visited
    '''
    hashtable = dict.fromkeys(array,False)
    length = len(array)
    if length == 1:
        return [array[0],array[0]]
    result = [float('+inf'), float('-inf')]
    for i in range(length):
        if all(hashtable.values()):
            return result
        hashtable[array[i]] = True
        cur = array[i]
        largest = result[1] - result[0]
        j = 1
        while True:
            # see if the number came before cur is in the hashtable
            test = cur-j
            if test in hashtable:
                hashtable[test] = True
                j += 1
            else:
                beg = test+1
                j = 1
                break
        while True:
            test = cur+j
            if test in hashtable:
                hashtable[test] = True
                j += 1
            else:
                end = test-1
                if largest < end - beg:
                    result[0], result[1] = beg, end
                break
    return result

array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(largestRange(array))