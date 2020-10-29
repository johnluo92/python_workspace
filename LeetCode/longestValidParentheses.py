# def longestValidParentheses(s: str) -> int:
#     paren = {'(':')'}
#     stack = []
#     dp = [0] * len(s)
    
#     for i in range(len(s)):
#         item = s[i]
#         if item in paren:
#             stack.append(item)
#         else:
#             if len(stack):
#                 if item == paren[stack.pop()]:
#                     dp[i] = dp[i-1] + 2
                
#     return max(dp)

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        if not s:
            return 0
        record = [0]*len(s)
        left = []
        for index, char in enumerate(s):
            print('index: {}, left: {}, record: {}'.format(index, left, record))
            if char == "(":
                left.append(index)
            elif left:
                leftIndex = left.pop()
                print('leftIdx: {}'.format(leftIndex))
                test = index - leftIndex
                biggerLeft = record[index-1]+1
                if index>0 and test == biggerLeft:
                    print('test: {}, biggerLeft: {}'.format(test, biggerLeft))
                    record[index] = record[index-1] + 2
                    if leftIndex > 0:
                        record[index] += record[leftIndex-1]
        return max(record)

a = "(()" # 2 
a = "()(()(()(()" # 2 
a = "()()(()" # 4
# a = "(())" # 4
# a = "()(()" # 2
ans = Solution()
print(ans.longestValidParentheses(a))

