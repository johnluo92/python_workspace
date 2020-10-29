# permutation of s in b
from itertools import permutations

def findPermutations(s, b):
    dic = dict.fromkeys([''.join(p) for p in permutations(s)])
    print(dic)
    leftPointer = 0
    rightPointer = len(s) - 1
    ans = []
    
    if len(b) < len(s):
        return 'no permutations'
    else:
        while rightPointer < len(b):
            if b[leftPointer:rightPointer+1] in dic:
                ans.append(b[leftPointer:rightPointer+1])
            leftPointer += 1
            rightPointer += 1
    return ans

s = 'abcb'
b = 'bcacbabbcaacbacbbcaaacbcb'

print(findPermutations(s,b))

# ---------------------------------------------------------------------------------------------------

def dyanmicFib(n):
    if n == 1 or n == 2:
        return 1
    
    fib = [0]*(n+1)
    
    fib[0] = 1
    fib[1] = 1
    
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    print(fib)
    return fib[n]

# print(dyanmicFib(8))

def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    count = 0
    for i in denoms:
        if i <= n:
            count += 1
    return count        
    
# print(numberOfWaysToMakeChange(6, [1,2,3,5,6]))

# V = ['a', 'b', 'c', 'd', 'e']
# E = ['ab', 'ac', 'bd', 'cd', 'de']
# dic = {}
# for i in range(len(V)):
#     dic[V[i]] = list(E[i])
    
# print(dic)
    
# dic = {k:v for (k,v) in zip(V,) for e in iter(E)}
# print(dic)

class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()
# Add the new edge

    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

# List the edge names
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)
g.AddEdge({'a','e'})
g.AddEdge({'a','c'})
print()
print(g.edges())

# ---------------------------------------------------------------------------------------------------

arr = ['p','e','r','f','e','c','t','',
'm','a','k','e','s','',
'p','r','a','c','t','i','c','e']

'''
arr = ['p','r','a','c','t','i','c','e','',
'm','a','k','e','s','',
'p','e','r','f','e','c','t']
'''

def reverseList(array):
    array.reverse()
    leftIdx = 0
    rightIdx = 0
    for i in range(len(array)):
        if array[i] != '':
            rightIdx += 1
        else:
            swap(array, leftIdx, rightIdx-1)
            leftIdx = i + 1
            rightIdx = i + 1
            
    swap(array, leftIdx, len(array)-1)
    return array

def swap(array, left, right):
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    print('test', array)
        
print(reverseList(arr))
# ---------------------------------------------------------------------------------------------------

# naive solution
# too slow

# https://leetcode.com/problems/daily-temperatures/submissions/

# class Solution:
#     def dailyTemperatures(self, T):
#         i = 1
#         ans = []
#         counter = 1
#         while len(T):
#             if i == len(T) and len(T):
#                 i = 1
#                 counter = 1
#                 T.pop(0)
#                 ans.append(0)
#             elif T[i] > T[0]:
#                 ans.append(counter)
#                 T.pop(0)
#                 i = 1
#                 counter = 1
#             else:
#                 i += 1
#                 counter += 1
#         return ans
    
    # a very very elegant solution:
# using stacks to and going backwards in the array
# add the last item to the stack, iterate backwards to see if
# the last item is bigger than the current temperature. If yes,
# get the index difference denoting the number of days in between
# the two temoeratures. If the last stack item isn't greater than the current temperature, we pop the stack and look for the next temperature until the stack is empty. The iteration takes us further backwards; if the current temperature has no temperature to compare to, we know there is no higher temperature in the indexes after the current temperature. So the number of days one has to wait on that date for a warmer date is going to remain at 0.

class Solution:
    def dailyTemperatures(self, T):
        stack = []
        result = [0 for i in range(len(T))]
        for i in range(len(T)-1, -1, -1):
            while stack:
                if T[i] < stack[-1][1]:
                    result[i] = stack[-1][0] - i
                    break
                else:
                    stack.pop()
            stack.append((i, T[i]))
        
        return result

T = [73, 74, 75, 71, 69, 72, 76, 73]
#your output should be [1, 1, 4, 2, 1, 1, 0, 0]

print(Solution().dailyTemperatures(T))
                    