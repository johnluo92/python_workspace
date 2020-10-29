class Solution:
    def isHappy(self, n):
        ans = n
        repeat = {}
        while ans != 1:
            ans = self.getHappy(ans)
            if ans in repeat:
                print(repeat)
                return False
            else:
                repeat[ans] = True
        if ans == 1:
            return True
    
    def getHappy(self, ans):
        newNum = 0
        for i in str(ans):
            newNum += int(i)**2
        print(newNum)
        return newNum


print(Solution().isHappy(123))