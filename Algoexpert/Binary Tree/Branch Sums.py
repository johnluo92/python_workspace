'''Branch Sums

Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.

A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.
'''


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    arr = []
    return getBranchSums(root, arr, 0)


def getBranchSums(root, arr, curSum):
    if root.left is None and root.right is None:
        curSum += root.value
        arr.append(curSum)
        return arr
    curSum += root.value
    if root.left:
        arr = getBranchSums(root.left, arr, curSum)
    if root.right:
        arr = getBranchSums(root.right, arr, curSum)
    return arr


myTree = BinaryTree(1)
myTree.left = BinaryTree(2)
myTree.right = BinaryTree(3)
myTree.right.right = BinaryTree(7)
myTree.right.left = BinaryTree(6)
myTree.left.left = BinaryTree(4)
myTree.left.right = BinaryTree(5)
myTree.left.right.left = BinaryTree(10)
myTree.left.left.left = BinaryTree(8)
myTree.left.left.right = BinaryTree(9)

print(branchSums(myTree))  # True
