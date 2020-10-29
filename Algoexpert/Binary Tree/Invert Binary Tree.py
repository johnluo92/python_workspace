'''Invert Binary Tree

Write a function that takes in a Binary Tree and inverts it.
The function should swap every left node in the tree for its correspomding right node.
'''

def invertBinaryTree(tree):
    # Write your code here.
	if not tree:
		return
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
	tree.left, tree.right = tree.right, tree.left
	return tree


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

print(invertBinaryTree(myTree)) # True