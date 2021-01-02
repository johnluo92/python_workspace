class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, node):
    # Write your code here.
    
    successor = inOrderTraversal(tree, node)
    return successor

def inOrderTraversal(tree, node):
    leftNode, rightNode = None, None
    
    if not tree.left and not tree.right:
        return tree.value
    
    if tree.left:
        leftNode = inOrderTraversal(tree.left, node)
        if leftNode == node:
            return tree.value
        else if tree.right:
            rightNode = inOrderTraversal(tree.right, node)
    
    if leftNode

myTree = BinaryTree(1)
myTree.left = BinaryTree(2)
myTree.right = BinaryTree(3)
myTree.left.left = BinaryTree(4)
myTree.left.right = BinaryTree(5)
myTree.left.left.left = BinaryTree(6)

print(nodeDepths(myTree, 5)) # True