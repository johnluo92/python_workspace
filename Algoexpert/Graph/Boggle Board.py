class SuffixTrie:
    def __init__(self, stringArr):
        self.root = {}
        self.endSymbol = "*"
        print('my tree instance: ', stringArr)
        for word in stringArr:
            self.populateSuffixTrieFrom(word)

    def populateSuffixTrieFrom(self, string):
        node = self.root
        print(node)
        for j in range(len(string)):
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
    
    def isAWord(self, string):
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        return self.endSymbol in node
    
    
def boggleBoard(board, words):
    
    # Write your code here.
    
    traversed = [[False for x in range(len(board[0]))] for x in range(len(board))]
    
    wordsDictionary = set()
    
    myTrie = SuffixTrie(words)
    
    ans = []
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            DFS_traverseBoard(board, wordsDictionary, traversed, i, j, myTrie)
    for i in traversed:
        print(i)
    return list(wordsDictionary)


def DFS_traverseBoard(board, wordsDictionary, traversed, i, j, myTrie, currentWord = ''):
    leftbound, upperbound = 0, 0
    rightbound, lowerbound = len(board[0]), len(board)

    if traversed[i][j]:
        return currentWord
    traversed[i][j] = True

    currentWord = currentWord + board[i][j]

    if myTrie.isAWord(currentWord):
        if currentWord and currentWord not in wordsDictionary:
            wordsDictionary.add(currentWord)
    
    if myTrie.contains(currentWord):

        if i - 1 >= upperbound:
            DFS_traverseBoard(board, wordsDictionary, traversed, i - 1, j, myTrie, currentWord)
        if j - 1 >= leftbound:
            DFS_traverseBoard(board, wordsDictionary, traversed, i, j - 1, myTrie, currentWord)
        if j + 1 < rightbound:
            DFS_traverseBoard(board, wordsDictionary, traversed, i, j + 1, myTrie, currentWord)
        if i + 1 < lowerbound:
            DFS_traverseBoard(board, wordsDictionary, traversed, i + 1, j, myTrie, currentWord)
            
        # left upper diagnol
        if i - 1 >= upperbound and j - 1 >= leftbound:
            DFS_traverseBoard(board, wordsDictionary, traversed, i - 1, j -1, myTrie, currentWord)
        # right upper diagnol
        if i - 1 >= upperbound and j + 1 < rightbound:
            DFS_traverseBoard(board, wordsDictionary, traversed, i - 1, j + 1, myTrie, currentWord)
        # left lower diagnol
        if i + 1 < lowerbound and j - 1 >= leftbound:
            DFS_traverseBoard(board, wordsDictionary, traversed, i + 1, j - 1, myTrie, currentWord)
        # right lower diagnol            
        if i + 1 < lowerbound and j + 1 < rightbound:
            DFS_traverseBoard(board, wordsDictionary, traversed, i + 1, j + 1, myTrie, currentWord)

    traversed[i][j] = False
    
board = [
    ["t", "h", "i", "s", "i", "s", "a"],
    ["s", "i", "m", "p", "l", "e", "x"],
    ["b", "x", "x", "x", "x", "e", "b"],
    ["x", "o", "g", "g", "l", "x", "o"],
    ["x", "x", "x", "D", "T", "r", "a"],
    ["R", "E", "P", "E", "A", "d", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["N", "O", "T", "R", "E", "-", "P"],
    ["x", "x", "D", "E", "T", "A", "E"]
  ]

board = [
  ["y", "g", "f", "y", "e", "i"],
  ["c", "o", "r", "p", "o", "u"],
  ["j", "u", "z", "s", "e", "l"],
  ["s", "y", "u", "r", "h", "p"],
  ["e", "a", "e", "g", "n", "d"],
  ["h", "e", "l", "s", "a", "t"]
]
words = [
    "this",
    "is",
    "not",
    "a",
    "simple",
    "boggle",
    "board",
    "test",
    "REPEATED",
    "NOTRE-PEATED"
  ]

words = [
  "san",
  "sana",
  "at",
  "vomit",
  "yours",
  "help",
  "end",
  "been",
  "bed",
  "danger",
  "calm",
  "ok",
  "chaos",
  "complete",
  "rear",
  "going",
  "storm",
  "face",
  "epual",
  "dangerous"
]

# board = [
#     ["a", "b", "c", "d", "e"],
#     ["f", "g", "h", "i", "j"],
#     ["k", "l", "m", "n", "o"],
#     ["p", "q", "r", "s", "t"],
#     ["u", "v", "w", "x", "y"]
#   ]

# words = ["agmsy", "agmsytojed", "agmsytojedinhcbgl", "agmsytojedinhcbfl"]

# board = [["a", "b"],
#         ["c", "d"]]

# words = ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "abca"]


print(boggleBoard(board, words))
# expected = ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
# expected = ["agmsy", "agmsytojed", "agmsytojedinhcbfl"]