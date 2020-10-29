'''Suffix Trie Construction
'''
# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.

# o(n^2) time | o(1) space
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        for i in range(len(string)):
            self.populateSuffixTrieFrom(i, string)

    def populateSuffixTrieFrom(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            char = string[j]
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        return self.endSymbol in node