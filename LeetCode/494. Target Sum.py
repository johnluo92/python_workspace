'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
 

Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''

import time

class Solution:
    
    counter = 0
    
    def findTargetSumWays(self, nums, S):
        
        self.ways_to_S(nums, S, 0, 0)
        
        ans = Solution.counter
        Solution.counter = 0
        print(ans)
        return ans
    
    def ways_to_S(self, nums, S, j, runningsum):
        if j == len(nums):
            if runningsum == S:
                Solution.counter += 1
                return True
            else:
                return False
        cond1 = self.ways_to_S(nums, S, j+1, runningsum-nums[j])
        cond2 = self.ways_to_S(nums, S, j+1, runningsum+nums[j])
        print(cond1 or cond2)
        
arr = [1,1,1,1,1]
t = 3
# arr = [25,29,23,21,45,36,16,35,13,39,44,15,16,14,45,23,50,43,9,15]
# t = 32
# arr = [6,20,22,38,11,15,22,30,0,17,34,29,7,42,46,49,30,7,14,5]
# t = 28
# 32
# start = time.time()
# Solution().findTargetSumWays(arr,t)
# end = time.time()
# print(end - start)


# --------------------------------------------------------------------------------

class Solution(object):
    def findTargetSumWays(self, nums, S):
        self.memo = {}
        print(self.ways_finder(nums, S))
        # print(self.memo)

    def ways_finder(self, nums, S):
        # print(nums, S)
        if (len(nums), S) in self.memo:
            return self.memo[(len(nums), S)]
        # print(nums, S)
        if nums == []:
            if S == 0:
                return 1
            else:
                return 0
        ans = self.ways_finder(nums[1:], S-nums[0]) + self.ways_finder(nums[1:], S+nums[0])
        # print(ans)
        self.memo[(len(nums), S)] = ans
        return ans


arr = [1,1,1,1,1]
t = 3
arr = [25,29,23,21,45,36,16,35,13,39,44,15,16,14,45,23,50,43,9,15]
t = 32
# arr = [6,20,22,38,11,15,22,30,0,17,34,29,7,42,46,49,30,7,14,5,2,3,4,5,7,8,43,2,6,59,8,4,35,64,7,8,5,33,45,53,3,4]
# t = 28
# 32
# print()
start = time.time()
Solution().findTargetSumWays(arr,t)
end = time.time()
print(end - start)