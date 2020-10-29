'''Powerset

Write a function that takes in an array of unique integers and returns its powerset.

The powerset P(X) of a set X is the set of all subsets of X. For example, the powerset of [1,2] is [[], [1], [2], [1,2]].

Note that the sets in the powerset do not need to be in any particular order'''

def powerset(array):
    # Write your code here.
    subsets = [[]]
    tracker = 0
    for element in array:
        for i in range(len(subsets)):
            tracker += 1
            currentSubset = subsets[i] # [] initial
            subsets.append(currentSubset + [element])
            print(len(subsets), i, subsets, tracker)
    return subsets
    
    
arr = ['a','b','c']
ans = powerset(arr)
print(ans)

'''
inner for loop:
range 1
[]
result = [] + [a]
[], [a]

range 2
[] + [b]
==> [], [a], [b]
[a] + [b] = [a,b]
== >[], [a], [b], [a,b]

range 4
[]
[] + [c]
== >[], [a], [b], [a,b], [c]
[a] + [c] = [a,c]
== >[], [a], [b], [a,b], [c], [a,c]
[b] + [c] = [b,c]
== >[], [a], [b], [a,b], [c], [a,c], [b,c]
[a,b] + [c] = [a,b,c]
== >[], [a], [b], [a,b], [c], [a,c], [b,c], [a,b,c]


'''

array = [1, 2, 3]
powerset(array) #[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]