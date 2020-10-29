import time

class Solution:
    
    counter = 0
    
    def uniquePaths(self, m: int, n: int) -> int:

        self.ways_helper(m, n, 0, 0)
        answer = Solution.counter
        # Solution.counter = 0
        print(Solution.counter)
        print('answer:', answer)
        return Solution.counter

    def ways_helper(self, m, n, i, j):
        lowerbound, rightbound = m, n

        if i == rightbound-1 and j == lowerbound-1:
            Solution.counter += 1
            return

        if i+1 < rightbound:
            self.ways_helper(m, n, i+1, j)
        if j+1 < lowerbound:
            self.ways_helper(m, n, i, j+1)

        return
    
    
arr = [[0 for col in range(3)] for row in range(3)]

start = time.time()

Solution().uniquePaths(12,12)

end = time.time()
print(end - start)
# [0,0,0]
# [0,0,0]
# [0,0,0]