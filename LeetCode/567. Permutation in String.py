class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        my_trie = Trie()
        my_trie.build_trie(s2)
        my_trie.build_reverse(s2)
        
        def getperms(temp, j, perms):
            if j == len(temp):
                perm = ''.join(temp)
                perms.append(perm)
                return
            
            for i in range(j, len(temp)):
                temp[i], temp[j] = temp[j], temp[i]
                getperms(temp, j+1, perms)
                temp[i], temp[j] = temp[j], temp[i]
        
        perms = []
        temp = list(s1)
        getperms(temp, 0, perms)
        for perm in perms:
            if my_trie.contains(perm):
                return True
        
        return False
        
class Trie:
    def __init__(self):
        self.root = {}
        self.end = '*'
        
    def build_trie(self, string2):
        for i in range(len(string2)):
            node = self.root
            for j in range(i, len(string2)):
                char = string2[j]
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[self.end] = True
            
    def build_reverse(self, string2):
        newstr = string2[::-1]
        for i in range(len(newstr)):
            node = self.root
            for j in range(i, len(newstr)):
                char = newstr[j]
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[self.end] = True
            
    def contains(self, string1):
        node = self.root
        for char in string1:
            if char in node:
                node = node[char]
            else:
                return False
        return True



s1, s2 = "rvwrk", "lznomzggwrvrkxecjaq" # wrvrk or krvrw

s1, s2 = "abcdxabcde", "abcdeabcdx"

"adc"
"dcda"

print(Solution().checkInclusion(s1,s2))