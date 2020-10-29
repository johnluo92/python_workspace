'''Output a list of anagrams given a group of words.
'''

def groupAnagrams(words):
    # Write your code here.
    '''
    This method also uses a hashtable, but more effectively so.
    
    The word is first added to its anagram key's value set
    if its anagram has not been put in the hashtable yet.
    The algo takes the current word in the iteration, and check
    to see if it exists in the keys of the anagrams hastable
    (in the keys). If its sorted version is in the key, then
    add the unsorted word to the key's value set (which is in a list)
    If no anagrams of a word is found, its key anagram contains
    just the unsorted word.
    
    Casting the values of the hashtable convert them to contained
    lists of anagram words in their original, unsorted versions.
    The key contains the sorted version of all anagrams.
    '''
    anagrams = {}
    for word in words:
        sortedWord = ''.join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())

words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
words = ['','']
print(groupAnagrams(words))