'''Move Element to End

You are given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers.
'''

# o(n) time | o(1) space
def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
    right = len(array) - 1
    
    while left < right:
        
        if array[left] == toMove and array[right] == toMove:
            right -= 1
            
        elif array[left] == toMove and array[right] != toMove:
            array[left], array[right] = array[right], array[left]
            right -= 1
            left += 1
            
        elif array[left] != toMove and array[right] == toMove:
            left += 1
            right -= 1
            
        else:
            left += 1
    return array


array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

print(moveElementToEnd(array,toMove))