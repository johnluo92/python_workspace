# find range
# https://www.algoexpert.io/questions/Search%20For%20Range

def searchForRange(array, target):
    # Write your code here.
    ans = []    
    ans = binarySearchHelper(array, target)
    return ans

def binarySearchHelper(array, target):
    if len(array) == 0:
        return [-1,-1]
    left = 0
    right = len(array)
    while left < right:
        mid = (left+right)//2
        leftIdx = mid - 1
        rightIdx = mid + 1
        if array[mid] == target:
            while leftIdx > -1 and array[leftIdx] == target:
                leftIdx -= 1
            while rightIdx < len(array) and array[rightIdx] == target:
                rightIdx += 1
            return [leftIdx+1, rightIdx-1]
        else:
            if array[mid] > target:
                right = mid
            else:
                left = mid+1
    return [-1, -1]

# ----------------------------------------------------------------------------------------

def searchForRange(array, target):
    ans = [-1, -1]
    binarySearchHelper(array, target, ans, 0, len(array), True)
    binarySearchHelper(array, target, ans, 0, len(array), False)
    return ans

def binarySearchHelper(array, target, ans, left, right, lookleft):
    mid = (left+right) // 2
    
    if left < right:
        print(array, lookleft, mid, left, right)
        if array[mid] > target:
            binarySearchHelper(array, target, ans, left, mid, lookleft)
        elif array[mid] < target:
            binarySearchHelper(array, target, ans, mid+1, right, lookleft)
        else:
            if lookleft:
                if mid-1 >= 0 and array[mid-1] == target:
                    binarySearchHelper(array, target, ans, left, mid, lookleft)
                else: ans[0] = mid
            elif not lookleft:
                if mid+1 < len(array) and array[mid+1] == target:
                    binarySearchHelper(array, target, ans, mid+1, right, lookleft)
                else: ans[1] = mid
    else:
        return
            
            
arr = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
# arr = [5, 7, 7, 8, 8, 10]
targ = 45
# targ = 9

print(searchForRange(arr, targ))

# ----------------------------------------------------------------------------------------

def searchForRange(array, target):
    ans = [-1, -1]
    binarySearchHelper(array, target, ans, 0, len(array), True)
    binarySearchHelper(array, target, ans, 0, len(array), False)
    return ans

def binarySearchHelper(array, target, ans, left, right, lookleft):   

    while left < right:
        mid = (left+right) // 2
        print(array, lookleft, mid, left, right)
        if array[mid] > target:
            right = mid
        elif array[mid] < target:
            left = mid+1
        else:
            if lookleft:
                if mid-1 >= 0 and array[mid-1] == target:
                    right = mid
                else:
                    ans[0] = mid
                    return
            elif not lookleft:
                if mid+1 < len(array) and array[mid+1] == target:
                    left = mid+1
                else:
                    ans[1] = mid
                    return
            
            
arr = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
arr = [5, 7, 7, 8, 8, 10]
targ = 45
targ = 9

print(searchForRange(arr, targ))