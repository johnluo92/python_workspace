'''Palindrome Check

Check if the string satisfies the conditions of being a palindrom
'''

def isPalindrome(string):
    # Write your code here.
    leftIdx = 0
    rightIdx = len(string)-1
    while leftIdx <= rightIdx:
        if string[leftIdx] == string[rightIdx]:
            leftIdx += 1
            rightIdx -= 1
        else:
            return False
    return True

string = "abcdcba"

print(isPalindrome(string))