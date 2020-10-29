class Trie:
	def __init__(self, string):
		self.root = {}
		self.endSymbol = '*'
		self.populateSuffix(string)

	def populateSuffix(self, string):
		node = self.root
		for j in range(len(string)):
			char = string[j]
			if char not in node:
				node[char] = {}
			node = node[char]
		node[self.endSymbol] = True

	def contains(self, string):
		node = self.root
		for i in range(len(string)):
			char = string[i]
			if char in node:
				node = node[char]
			else:
				return False
		return True

	def hasWord(self, string):
		node = self.root
		for i in range(len(string)):
			char = string[i]
			if char in node:
				node = node[char]
			else:
				return False
		return self.endSymbol in node

myTrie = Trie('john')
print(myTrie.root)
print(myTrie.contains('john'))
print(myTrie.hasWord('joh'))

# --------------------------------------------------------------

with open('output.txt', 'w') as f:
    f.write('Hi there!')


class Solution:
    def groupAnagrams(self, strs):
        
        # Input: strs = ["eat","tea","tan","ate","nat","bat"]
        # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        
        myAnagrams = []
        
        dictionary = {''.join(sorted(k)) for k in strs}
        print(dictionary)

        for sortedItem in dictionary:
        	currentAna = []
        	for item in strs:
	        	if ''.join(sorted(item)) in dictionary:
	        		currentAna.append(item)
	        	myAnagrams.append(currentAna)

		    print(myAnagrams)



Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]