'''Find Closest Value in BST

Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value to that target value contained in the BST.

You can assume that there will be only one closest value.

Each BST node has a integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater to every node to its left; its value is less than or equal to the values of every node to the its right; and its children nodes are either valid BST nodes themselves or None / null.
'''

# o(n) time | o(n) space
def findClosestValueInBst(tree, target):
	# Write your code here.
	closestVal = tree.value
	smallestDiff = float('inf')
	while tree:
		if tree.value == target:
			return tree.value
		diff = abs(target - tree.value)
		if diff < smallestDiff:
			smallestDiff = diff
			closestVal = tree.value
		if target > tree.value and tree.right:
			tree = tree.right
		elif target < tree.value and tree.left:
			tree = tree.left
		else:
			break	
	return closestVal

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

	#		10
	#	   /  \
	#	  9	   13
	
	#		10
	#	   /  \
	#	  5	  15
	#		 /  \
	#		13  22
	#		  \
	#	 	   14

myTree = BST(10)
myTree.left = BST(5)
myTree.right = BST(15)
myTree.right.right = BST(22)
myTree.right.left = BST(13)
myTree.right.left.right = BST(14)
myTree.left.left = BST(2)
myTree.left.right = BST(5)
myTree.left.left.left = BST(1)

print(findClosestValueInBst(myTree, 12)) # True