# nth digit
import time

class Solution:
    def findNthDigit(self, n: int) -> int:
        num_string = ''
        
        for i in range(1, n+1):
            if i > len(num_string):
                break
            num_string += str(i)
            # print(num_string)
            
        print(num_string[n-1])
        return num_string[n-1]


n = 10000

# 27 = 8
# 28 = 1
# 29 = 9
# 30 = 2
# 31 = 0
# 32 = 2
# 33 = 1
# 34 = 3

start = time.time()

Solution().findNthDigit(n)

end = time.time()

print(end-start)