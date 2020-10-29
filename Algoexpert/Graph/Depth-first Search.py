'''Depth-first Search

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
'''

class Node:
	def __init__(self, name):
		self.children = []
		self.name = name

	def addChild(self, name):
		self.children.append(Node(name))
		return self

	def depthFirstSearch(self, array):
		# Write your code here.
		array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
		print(array)
		return array

myTree = Node(1)
myTree.addChild(2)
myTree.addChild(3)
myTree.addChild(4)
myTree.addChild(5)
myTree.addChild(6)
myTree.depthFirstSearch([])