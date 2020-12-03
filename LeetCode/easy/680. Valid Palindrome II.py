class Solution:
    def validPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1
        
        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return s[L+1:R+1] == s[L+1:R+1][::-1] or s[L:R] == s[L:R][::-1]
        return True