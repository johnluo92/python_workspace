'''Node Detpths

The distance between a node in a Binary Tree and the tree's root is called the node's depth.

Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.
'''

def nodeDepths(root):
    # Write your code here.
	ans = 0Í
	ans = getAllDepths(root, ans, 0)
	return ans

def getAllDepths(root, ans, depth):
	ans += depth
	if root.left:
		ans = getAllDepths(root.left, ans, depth+1)
	if root.right:
		ans = getAllDepths(root.right, ans, depth+1)
	return ans

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

myTree = BinaryTree(10)
myTree.left = BinaryTree(5)
myTree.right = BinaryTree(15)
myTree.right.right = BinaryTree(22)
myTree.right.left = BinaryTree(13)
myTree.right.left.right = BinaryTree(14)
myTree.left.left = BinaryTree(2)
myTree.left.right = BinaryTree(5)
myTree.left.left.left = BinaryTree(1)

print(nodeDepths(myTree)) # True