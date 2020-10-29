'''Longest Palindromic Substring

Find the longest palindrome in a string
'''

def longestPalindromicSubstring(string):
    # Write your code here.
    leftbound = rightbound = 0
    result = string[0]
    length = len(string)
    test = ''
    for i in range(length):
        expand = True
        leftbound = i-1
        rightbound = i+1
        while leftbound >= 0 and rightbound < len(string):
            while rightbound <= len(string) and string[i] == string[rightbound] and expand:
                test = string[i:rightbound+1]
                if rightbound == length-1:
                    break
                rightbound += 1
            if string[leftbound] == string[rightbound]:
                test = string[leftbound:rightbound+1]
                leftbound -= 1
                rightbound += 1
                expand = False
            else:
                break
                
        if len(test) > len(result):
            result = test
                
    return result

string = "abaxyzzyxf"

print(longestPalindromicSubstring(string))