class Solution:
    def groupAnagrams(self, strs):
        
        # Input: strs = ["eat","tea","tan","ate","nat","bat"]
        # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        anagrams = {}
        for word in strs:
          sorted_word = ''.join(sorted(word))
          if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
          else:
            anagrams[sorted_word] = [word]

        anagrams = list(anagrams.values())
        print(anagrams)
        
strs = ["eat","tea","tan","ate","nat","bat"]   
# strs = ['','']   
print(Solution().groupAnagrams(strs))

## Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]