'''Validate BST

Write a function that takes in a potentially invalid Binary Search Tree (BST) and returns a boolean representing whether the BST is valid.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisifies the BST property.
'''

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
    # Write your code here.
	return validateHelper(tree, float('-inf'), float('inf'))
	
def validateHelper(tree, lowVal, highVal):
	if tree is None:
		return True
	else:
		val = tree.value
		if val < lowVal or val >= highVal:
			return False
		leftTree = validateHelper(tree.left, lowVal, val)
		rightTree = validateHelper(tree.right,val, highVal)
	return leftTree and rightTree

# ------------------------------------------------------
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
    # Write your code here.
	return validateBSTHelper(tree, float('-inf'), float('inf'))

def validateBSTHelper(tree, smallest, largest):
    if not tree:
		return True
	if tree.value >= largest:
		return False
	if tree.value < smallest:
		return False
	return validateBSTHelper(tree.left, smallest, tree.value) and validateBSTHelper(tree.right, tree.value, largest)

myTree = BST(10)
myTree.left = BST(5)
myTree.right = BST(15)
myTree.right.right = BST(22)
myTree.right.left = BST(13)
myTree.right.left.right = BST(14)
myTree.left.left = BST(2)
myTree.left.right = BST(5)
myTree.left.left.left = BST(1)

print(validateBst(myTree))