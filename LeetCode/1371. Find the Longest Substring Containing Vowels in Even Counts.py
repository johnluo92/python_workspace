import sys

class Solution:
    def findTheLongestSubstring(self, s):
        vowels = {'a','e','i','o','u'}
        vowel_count = [[char,True] if s.count(char)%2 == 0 else [char,False] for char in vowels]
        all_even = all([x[1] for x in vowel_count])
    
        if all_even:
            return len(s)
        x, y = 0, len(s)
        while not all_even:
            print(x,y)
            x,y = self.getLongest(s, vowel_count, x, y)
            vowel_count = [[char,True] if s[x:y].count(char)%2 == 0 else [char,False] for char in vowels]
            all_even = all([x[1] for x in vowel_count])
        
        return y-x
            
    def getLongest(self, s, vowel_count, x, y):
        def get_uneven(vowel_count):
            for pair in vowel_count:
                if pair[1] is False:
                    return pair[0]
                    
        def get_new_indexes(s, vowel_to_remove, x, y):
            disFromLeft = s[x:y].find(vowel_to_remove) - x
            # if disFromLeft == 0: disFromLeft += 1
            disFromRight = y - s[x:y].rfind(vowel_to_remove)
            # if disFromRight == 0: disFromRight -= 1
            fromLeft = disFromLeft < disFromRight

            if fromLeft:
                return disFromLeft, y
            else:
                return x, y-disFromRight
        
        vowel_to_remove = get_uneven(vowel_count)
        return get_new_indexes(s, vowel_to_remove, x, y)
        
s = "eleetminicoworoep"
s= "leetcodeisgreat"
print(Solution().findTheLongestSubstring(s)) # 13
print('done')