'''Output a list of anagrams given a group of words.
'''

# o(n^2) time | o(1) space
import string as st

def longestSubstringWithoutDuplication(string):
    # Write your code here.
    cur_longest = [0,1]
    d = dict.fromkeys(st.ascii_lowercase, True)
    length = len(string)

    for i in range(length):
        d[string[i]] = False
        j = i+1
        for j in range(j, length):
            while j<length and d[string[j]]:
                d[string[j]] = False
                j += 1
            test = [i,j]
            cur_longest = max(cur_longest, test, key=lambda x: x[1]-x[0])
            d = dict.fromkeys(st.ascii_lowercase, True)
            break
    
    return string[cur_longest[0]:cur_longest[1]]

# -------------------------------------------------

# o(n) time | o(1) space
def longestSubstringWithoutDuplication(string):
    # Write your code here.
    lastSeen = {}
    indexOfLongest = [0,0]
    startIdx = 0
    for index, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char]+1)
        if indexOfLongest[1] - indexOfLongest[0] < index - startIdx:
            indexOfLongest = [startIdx, index]
        lastSeen[char] = index
        
    first = indexOfLongest[0]
    second = indexOfLongest[1]
    return string[first:second+1]

print(longestSubstringWithoutDuplication('clementisacap'))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)
        if not len(s):
            return 0
        lastSeen = {}
        startIdx = 0
        longest = 0
        
        for i in range(len(s)):
            char = s[i]
            if char in lastSeen:
                startIdx = max(lastSeen[char]+1, startIdx)
            if i - startIdx > longest:
                longest = max(longest, i - startIdx)
            lastSeen[char] = i
            
        longest += 1
        print(longest)
        return longest

string = 'bbcabcbb'
string = 'bbbbb'
string = 'pwwkew'
string = 'au'
string = "abba"
# string = 'aabc'
Solution().lengthOfLongestSubstring(string)