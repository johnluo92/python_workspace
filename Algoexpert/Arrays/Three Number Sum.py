'''Three Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimentional array of all these triplets. The numbers in each triplet should be ordered in asending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up the target sum, the function should return an empty array'''

# o(n^2) time | o(n) space
def threeNumberSum(array, targetSum):
    # Write your code here.
    workingArray = sorted(array)
    # [-8, -6, 1, 2, 3, 5, 6, 12] #
    length = len(workingArray)
    
    ans = []
    for i in range(length-2):
        
        leftIdx = i+1
        rightIDx = length - 1
        
        while leftIdx < rightIDx:
            
            frs_num = workingArray[i]
            sec_num = workingArray[leftIdx]
            trd_num = workingArray[rightIDx]
            testSum = frs_num + sec_num + trd_num
            
            if targetSum > testSum:
                leftIdx += 1
            elif targetSum < testSum:
                rightIDx -= 1
            elif targetSum == testSum:
                ans.append([frs_num, sec_num, trd_num])
                leftIdx += 1
                rightIDx -= 1
    return ans

array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSum(array,targetSum))