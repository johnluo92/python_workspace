def minHeightBst(array):
    newArray = []
    insertArray = minHeightArray(array, newArray)
    print('Queue of list to insert:', insertArray)
    myTree = BST(insertArray.pop(0))
    while len(insertArray) > 0:
        myTree.insert(insertArray.pop(0))
    return myTree

def minHeightArray(array, newarray):
    if not array:
        return
    mid = (len(array) // 2)
    newarray.append(array[mid])
    minHeightArray(array[:mid],newarray)
    minHeightArray(array[mid+1:],newarray)
    return newarray

def preOrderTraverse(tree, array): # 5, 3, 2, 4, 7
    # Write your code here.
    array.append(tree.value)
    if tree.left:
        preOrderTraverse(tree.left, array)
    if tree.right:
        preOrderTraverse(tree.right, array)
    return array

def getLevelAverage(tree):
    dic = {}
    print('dic before', dic)
    if tree:
        helperDepth(tree, dic)
    ans = []
    for i in dic:
        ans.append(sum(dic[i])/len(dic[i]))
    print('my depths', dic)
    return ans

def helperDepth(tree, dic, depth = 0):
    if not tree:
        return
    if depth not in dic:
        dic[depth] = [tree.value]
    else:
        dic[depth].append(tree.value)
    
    helperDepth(tree.left, dic, depth+1)
    helperDepth(tree.right, dic, depth+1)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
                
#            5
#           / \
#          3   7
#         / \
#        2   4
# arr = [3, 2, 4, 7]


#             13
#           /    \
#          7     15
#         / \    / \
#        5  10  14  22
#       /
#      2
arr = [2, 5, 7, 10, 13, 14, 15, 22]
tree = minHeightBst(arr)

# newTree = BST(5)
# for i in arr:
#     newTree.insert(i)

print()
print()
ans = getLevelAverage(tree)
print('average of each level from the root: ', ans)