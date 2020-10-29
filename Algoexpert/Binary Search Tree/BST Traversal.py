'''BST Traversal

Write three functions that take in a Binary Search Tree (BST) and an empty array, traverse the BST, add its nodes' values to the input array, and return that array. The three functions should traverse the BST using the in-order, pre-order, and post-order tree-traversal techniques, respectively.

BST has to satisfy the conditions of being a BST node (left child smaller or equal to the root's, and right child being greater than the root's value.)
'''

def inOrderTraverse(tree, array):
    # Write your code here.
	if tree.left:
		inOrderTraverse(tree.left, array)
	array.append(tree.value)
	if tree.right:
		inOrderTraverse(tree.right, array)
	return array

def preOrderTraverse(tree, array):
    # Write your code here.
	array.append(tree.value)
	if tree.left:
		preOrderTraverse(tree.left, array)
	if tree.right:
		preOrderTraverse(tree.right, array)
	return array

def postOrderTraverse(tree, array):
    # Write your code here.
	if tree.left:
		postOrderTraverse(tree.left, array)
	if tree.right:
		postOrderTraverse(tree.right, array)
	array.append(tree.value)
	return array
