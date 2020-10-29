class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class BST_Class(object):
	def __init__(self):
		self.root = None

	def isValidBST(self, n):
		return self._is_valid_helper(n, float('-inf'), float('inf'))

	def _is_valid_helper(self, n, low, high):
		if not n:
			return True

		val = n.val

		if ((n.val >= low and n.val <= high) and
			self._is_valid_helper(n.left, low, n.val) and # validate left subtree
			self._is_valid_helper(n.right, n.val, high)): # validate right subtree
			return True
		return False

def inOrderTraverse(tree, array): # 2, 3, 4, 5, 7
	if tree.left:
		inOrderTraverse(tree.left, array)
	array.append(tree.val)
	if tree.right:
		inOrderTraverse(tree.right, array)
	return array

def preOrderTraverse(tree, array): # 5, 3, 2, 4, 7
	# Write your code here.
	array.append(tree.val)
	if tree.left:
		preOrderTraverse(tree.left, array)
	if tree.right:
		preOrderTraverse(tree.right, array)
	return array

def postOrderTraverse(tree, array): # 2, 4, 3, 7, 5
	# Write your code here.
	if tree.left:
		postOrderTraverse(tree.left, array)
	if tree.right:
		postOrderTraverse(tree.right, array)
	array.append(tree.val)
	return array


def findKthSmallest(tree, k):
    ans = []
    ans = inOrderTraverse(tree, ans)
    print(ans)
    k = k-1
    return ans[k+1]

#			5
#		   / \
#		  3   7
#		 / \
#		2   4

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.right.left = Node(7)
node.right.right = Node(7)
node.right.right.right = Node(4)
node.right.right.right.left = Node(6)
node.left.left = Node(4)
node.left.left.right = Node(9)
node.left.left.right.left = Node(2)
node.left.left.right.right = Node(3)
node.left.left.right.right.right = Node(4)
node.left.left.right.right.right.left = Node(2)

# node = Node(1)
# node.right = Node(2)
# node.right.right = Node(3)
# node.right.right.right = Node(4)

myTree = BST_Class()
myTree.root = node

print(myTree.isValidBST(node))

array = []
preorder = preOrderTraverse(myTree.root, array)
print(preorder, "(pre-order traversal)")

array = []
inorder = inOrderTraverse(myTree.root, array)
print(inorder, "(in-order traversal)")

array = []
postOrder = postOrderTraverse(myTree.root, array)
print(postOrder, "(post-order traversal)")

print(findKthSmallest(myTree.root, 4)) # 2, 3, 4, 5, 7

