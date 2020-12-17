import sys
class Solution:
    def findTheLongestSubstring(self, s):
        vowels = {'a','e','i','o','u'}
        vowel_count = [[char,True] if s.count(char)%2 == 0 else [char,False] for char in vowels]
        all_even = all([x[1] for x in vowel_count])
        if len(s) == 1 and not all_even:
            return 0
    
        if all_even:
            return len(s)
        else:
            new_str = self.getLongest(s, vowel_count)
            return self.findTheLongestSubstring(new_str)
            
    def getLongest(self, s, vowel_count):
        
        def get_uneven(vowel_count):
            for pair in vowel_count:
                if pair[1] is False:
                    return pair[0]
                    
        def get_new_indexes(s, vowel_to_remove):
            print(s)
            x, y = 0, len(s)
            from_left = s.find(vowel_to_remove)
            from_right = s.rfind(vowel_to_remove)
        
            leftDistance = from_left-x
            rightDistance = y-from_right
            if leftDistance == 0:
                print(s[x+1:y])
                return s[x+1:y]
            elif rightDistance == 1:
                return s[x:y-1]
            if rightDistance > leftDistance:
                return s[from_left+1:y]
            else:
                return s[x:from_right]

        vowel_to_remove = get_uneven(vowel_count)
        return get_new_indexes(s, vowel_to_remove)
        
s = "eleetminicoworoep" #13
s = "leetcodeisgreat" #5
# s = "id" # 1
print(Solution().findTheLongestSubstring(s)) # 13
print('done')