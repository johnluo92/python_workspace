'''Multi String Search

Write a function that takes in a big string and an array of small strings, all of which are smaller in length than the big string. The function should return an array of booleans, where each boolean represents whether the small string at that index in the array of small strings is contained in the big string.
'''

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.

# o(n * w^2) | o(n * w^2)
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        stringArr = string.split(' ')
        print(stringArr)
        for word in stringArr:
            for i in range(len(word)):
                self.populateSuffixTrieFrom(i, word)

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
        return True

def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    myTrie = SuffixTrie(bigString)
    ans = [None for x in range(len(smallStrings))]
    i = 0
    for substring in smallStrings:
        ans[i] = myTrie.contains(substring)
        i += 1

    print(myTrie.root)
    return ans

bigString = "this is a big string"
smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]

print(multiStringSearch(bigString, smallStrings))
