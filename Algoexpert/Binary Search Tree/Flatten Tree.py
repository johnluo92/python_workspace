# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    # Write your code here.
	
	head = flattenTreeHelper(root)
	while head.left:
		head = head.left
	return head

def flattenTreeHelper(root, prev=None):
	if root:
		prev = flattenTreeHelper(root.left, prev)

		if prev is not None:
			prev.right = root
			root.left = prev
			prev = root
		else:
			prev = root

		prev = flattenTreeHelper(root.right, prev)
	return prev


myTree = BinaryTree(1)
myTree.left = BinaryTree(2)
myTree.left.left = BinaryTree(4)
myTree.left.right = BinaryTree(5)
myTree.left.right.left = BinaryTree(7)
myTree.left.right.right = BinaryTree(8)
myTree.right = BinaryTree(3)
myTree.right.left = BinaryTree(6)

head = flattenBinaryTree(myTree) 
while head:
	print(head.value, end = ', ')
	head = head.right

# 4 <-> 2 <-> 7 <-> 5 <-> 8 <-> 1 <-> 6 <-> 3 <-> 3