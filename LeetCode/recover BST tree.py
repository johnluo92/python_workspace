https://codeinterview.io/YNMNRFDOBD

#recover BST tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        
        # 3, 2, 1
        # 1, 2, 3
        
        # 1, 3, 2, 4
        # 1, 2, 3, 4
        
        inOrderTree = []
        switchCandidates = []
        self.getInOrderTree(root, inOrderTree)
        for i in range(1, len(inOrderTree)):
            if inOrderTree[i].val < inOrderTree[i-1].val:
                switchCandidates.append(inOrderTree[i-1])
                break
        for i in reversed(range(len(inOrderTree)-1)):
            if inOrderTree[i].val > inOrderTree[i+1].val:
                switchCandidates.append(inOrderTree[i+1])
                
        switchCandidates[0].val, switchCandidates[1].val = switchCandidates[1].val, switchCandidates[0].val

        for tree in inOrderTree:
            print(tree.val)
        
    def getInOrderTree(self, root, inOrderTree):
        if not root:
            return
        if root.left:
            self.getInOrderTree(root.left, inOrderTree)
        inOrderTree.append(root)
        if root.right:
            self.getInOrderTree(root.right, inOrderTree)
        return


myTree = TreeNode(3)
myTree.left = TreeNode(1)
myTree.right = TreeNode(4)
myTree.right.left = TreeNode(2)

mySolution = Solution()
mySolution.recoverTree(myTree)



# ---------------------------------------------------------------

#   3
#  / \
# 1   4
#    /
#   2


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:

        inOrderTree = []
        self.getInOrderTree(root, inOrderTree)

        print(inOrderTree)
        
        self.findInvalids(root, float('-inf'), float('inf'), None, None)

        inOrderTree = []
        self.getInOrderTree(root, inOrderTree)

        print(inOrderTree)

    def getInOrderTree(self, root, inOrderTree):
        if root:
            self.getInOrderTree(root.left, inOrderTree)
            inOrderTree.append(root.val)
            self.getInOrderTree(root.right, inOrderTree)
        return
    
    def findInvalids(self, root, low, high, smallest, largest):
        
        if not root:
            return
        
        if root.val < low:
            root.val, smallest.val = smallest.val, root.val
            print(root.val)
            return
        if root.val > high:
            print(root.val)
            root.val, largest.val = largest.val, root.val
            print(root.val)
            return
        if root.left and root.right:
            if root.left.val > root.right.val:
                root.left.val, root.right.val = root.right.val, root.left.val
        
        largest = root
        self.findInvalids(root.left, low, root.val, smallest, largest)
        smallest = root
        self.findInvalids(root.right, root.val, high, smallest, largest)


# myTree = TreeNode(3)
# myTree.left = TreeNode(1)
# myTree.right = TreeNode(4)
# myTree.right.left = TreeNode(2)

#   2
#  / \
# 3   1

#   2
#  / \
# 1   3

# myTree = TreeNode(2)
# myTree.left = TreeNode(3)
# myTree.right = TreeNode(1)

# -----

#   3
#    \
#     2
#      \
#       1

#   1
#    \
#     2
#      \
#       3

myTree = TreeNode(3)
myTree.right = TreeNode(2)
myTree.right.right = TreeNode(1)

mySolution = Solution()
mySolution.recoverTree(myTree)