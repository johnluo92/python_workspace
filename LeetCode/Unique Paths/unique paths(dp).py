import time

class Solution:
    
    counter = []
    
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        matrix = [[1 for col in range(n)] for row in range(m)]

        # for row in matrix:
        #     print(row)
        # print()

        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = matrix[row][col-1] + matrix[row-1][col]

      
        # for row in matrix:
        #     print(row)
        # print()

        print(matrix[-1][-1])

start = time.time()

Solution().uniquePaths(1000,1000)

end = time.time()
print(end - start)
# [0,0,0]
# [0,0,0]
# [0,0,0]