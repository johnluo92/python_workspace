'''BST Construction

Write a BST class for binary search tree.
'''


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # o(log(n)) time | o(n) space
    # worse o(n) time | o(b) space
    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		if value < self.value:
			if self.left:
				self.left.insert(value)
			else:
				self.left = BST(value)
		else:
			if self.right:
				self.right.insert(value)
			else:
				self.right = BST(value)
        return self

    # o(log(n)) time | o(n) space
    # worse o(n) time | o(b) space
    def contains(self, value):
        # Write your code here.
		if value < self.value:
			if self.left is None:
				return False
			else:
				return self.left.contains(value)
		elif value > self.value:
			if self.right is None:
				return False
			else:
				return self.right.contains(value)
		else:
			return True

    # o(logn) time | o(logn) space
    # worse o(n) time | o(b) space
    def remove(self, value, parentNode = None):
        # Write your code here.
        # Do not edit the return statement of this method.
        node = self
        while node:
            if value < node.value:
                parentNode = node
                node = node.left
            elif value > node.value:
                parentNode = node
                node = node.right
            else:
                if node.left and node.right:
                    node.value = node.right.getMinVal()
                    node.right.remove(node.value, node)
                elif parentNode is None:
                    if node.left:
                        node.value = node.left.value
                        node.right = node.left.right
                        node.left = node.left.left
                    elif node.right:
                        node.value = node.right.value
                        node.left = node.right.left
                        node.right = node.right.right
                    else:
                        node.value = None
                elif parentNode.left == node:
                    parentNode.left = node.left if node.left else node.right
                elif parentNode.right == node:
                    parentNode.right = node.right if node.right else node.left
                break
                    
        return self

    def getMinVal(self):
        node = self
        while node.left:
            node = node.left
        return node.value
