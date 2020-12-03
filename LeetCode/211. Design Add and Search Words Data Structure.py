class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = '*'
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[True] = {}
        

    def search(self, word: str, i = 0, node = None) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if node is None:
            node = self.root
        if i == len(word):
            return True in node
            
        for j in range(i, len(word)):
            char = word[j]
            if char == '.' and len(node):
                for key in node:
                    if self.search(word, j+1, node[key]):
                        return True
                return False
            elif char in node:
                node = node[char]
            else:
                return False
        return True in node

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
[[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
# output [null,null,null,true,true,false,true,false,true]
# expected [null,null,null,true,true,false,true,false,false]



["WordDictionary",  [[],
"addWord",          ["a"],
"addWord",          ["a"], 
"search",           ["."],
"search",           ["a"],
"search",           ["aa"],
"search",           ["a"],
"search",           [".a"],
"search"]           ["a."]]


["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]


["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]



