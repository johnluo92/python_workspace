def shiftedBinarySearch(array, target):
    # Write your code here.
    return shiftHelper(array, target, 0, len(array))

def shiftHelper(array, target, L, R):
    
    while L < R:
        
        mid = (L+R)//2

        if array[mid] < target:

            if array[L] <= target and array[L] >= array[mid]:
                R = mid
            else:
                L = mid + 1

        elif array[mid] > target:

            if array[L] <= target and array[L] <= array[mid]:
                R = mid
            else:
                L = mid+1
        else:
            ans = 'found at index: {}'.format(mid)
            return ans
        
    return -1
    
    # [45, 61, 71, 72, 73,     0,     1, 21, 33, 37]
    
    # [45, 61, 71, 72, 73,     74,     0, 21, 33, 37, 45]
    
   # [45, 45, 61, 71, 72,     73,     74, 0, 1, 21, 33]
    
    # [72, 73, 0, 1, 21,     33,     37, 45, 61, 71]
    
arr = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
print(shiftedBinarySearch(arr,21))