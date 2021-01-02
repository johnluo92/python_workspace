class Solution:
    def canReach(self, arr, start): #bool
        traversing = set()
        return self.searchForZero(arr, start, traversing)
        
    def searchForZero(self, arr, curIdx, traversing):
        if arr[curIdx] == 0:
            return True

        if curIdx in traversing:
            return False
        traversing.add(curIdx)

        forward = curIdx + arr[curIdx]
        backward = curIdx - arr[curIdx]

        if forward <= len(arr)-1:
            if self.searchForZero(arr, forward, traversing): return True

        if backward >= 0:
            if self.searchForZero(arr, backward, traversing): return True

        return False

arr = [3,0,2,1,2]
start = 2
Solution().canReach(arr, start)

arr = [4,2,3,0,3,1,2]
start = 0
Solution().canReach(arr, start)

arr = [4,2,3,0,3,1,2]
start = 5
Solution().canReach(arr, start)