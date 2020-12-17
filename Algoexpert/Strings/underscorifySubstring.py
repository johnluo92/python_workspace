def underscorifySubstring(string, substring):
    # Write your code here.
    my_arr = string.split(' ')
    ans = ''
    for word in my_arr:
        new_word = get_underscore_word(word, substring)
        ans = ans + new_word + ' '
        
    print(ans)
    return ans.strip()

def get_underscore_word(word, substring):
    if len(word) < len(substring):
        return word
    slow_idx, str_idx = 0, 0
    idx_arr = []
    
    for i in range(len(word)):
        char = word[i]
        substr_char = substring[str_idx]
        if char == substr_char:
            str_idx += 1
            if str_idx == len(substring):
                idx_arr.append(slow_idx)
                slow_idx = i
                str_idx = 0
                idx_arr.append(i+1)
    
    if not len(idx_arr):
        return word
    
    for i in range(len(idx_arr)):
        if idx_arr[i] is not False and i + 1 <len(idx_arr):
            left, right = idx_arr[i], idx_arr[i+1]
            if left+right < len(substring) or left >= right:
                idx_arr[i], idx_arr[i+1] = False, False
                
    ans = ''
    print(word, idx_arr, end=' ')
    for i in range(len(word)):
        if idx_arr[0] is False:
            idx_arr.pop(0)
        if len(idx_arr) and idx_arr[0] == i:
            idx_arr.pop(0)
            ans += '_'
        if not len(idx_arr):
            ans += word[i:]
            break
        ans += word[i]
    if len(idx_arr):
        ans += '_'
    print(idx_arr, ans)
    
    return ans

string = "testthis is a testtest to see if testestest it works"
string = "testthis is a testest to see if testestes it works"
#        "_test_this is a _testtest_ to see if _testestest_ it works"
substring = "test"
print('first attempt:\n')
underscorifySubstring(string, substring)



# {
#   "string": "testthis is a testest to see if testestes it works"
#   "substring": "test"
# }

# ans =     "_test_this is a _testest_ to see if _testest_es it works"
# myans =   "_test_this is a _test_est to see if _test_estes it works"


# ---------------------------------------------------------------------------


# second try:
print('\nsecond attempt:\n')

import sys

def underscorifySubstring(string, substring):
    # Write your code here.
    substrIndices = []
    i, sublen = 0, len(substring)
    
    while i < len(string):
        
        idx = string.find(substring, i)
        i = idx + 1
        
        if idx != -1:
            substrIndices.append([idx, idx+len(substring)])
        else:
            break
    print(substrIndices)
    
    underscoreIdx = constructIntervals(substrIndices, sublen)
    
    newstring_arr = []
    
    for i in range(len(string)):
        char = string[i]
        if underscoreIdx:
            if i == underscoreIdx[0]:
                newstring_arr.append('_')
                underscoreIdx.pop(0)
        newstring_arr.append(char)
        
    if underscoreIdx:
        newstring_arr.append('_')
    
    newstr = ''.join(newstring_arr)
    print(newstr)
    
def constructIntervals(substrIndices, sublen):
    newidxs = []
    
    interval1 = substrIndices.pop(0)
    
    while substrIndices:
        interval2 = substrIndices.pop(0)
        if interval1[1] + sublen >=  interval2[1]:
            interval1[1] = interval2[1]
        else:
            newidxs.append(interval1[0])
            newidxs.append(interval1[1])
            interval1 = interval2
    newidxs.append(interval1[0])
    newidxs.append(interval1[1])
    
    print(newidxs)
    # sys.exit(0)
    return newidxs
        
    
string = "idktestthis is a testtest to see if testestest it works"
        # "_test_this is a _testtest_ to see if _testestest_ it works"
substring = "test"

# string = "this is a test to see if it works and test"
#         # "this is a _test_ to see if it works and _test_"
# substring = "test"


underscorifySubstring(string, substring)