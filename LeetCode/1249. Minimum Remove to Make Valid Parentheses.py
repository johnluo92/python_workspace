# 1249. Minimum Remove to Make Valid Parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # explanation keep track of all the invalid parentheses indexes (left to right)
        # loop through input string, check if that index is the first in the queue that holds the invalid parentheses, if yes pop from the queue (left pop), if not then add that char to an anwer string.
        
        stack, to_remove = [], []
        ht = {'(' : ')'}
        
        for i in range(len(s)):
            char = s[i]
            if char in ht:
                stack.append(i)
            elif char == ht['(']:
                if len(stack):
                    stack.pop()
                else:
                    to_remove.append(i)
                    
        if len(stack):
            to_remove += stack
        
        result = ''
        for i in range(len(s)):
            if len(to_remove):
                if i == to_remove[0]:
                    to_remove.pop(0)
                    continue
                else:
                    result += s[i]
            else:
                result += s[i:]
                break
                
        print(result)
        return result



s = "lee(t(c)o)de)"
s = "))(("
s = "(a(b(c)d)"
Solution().minRemoveToMakeValid(s)