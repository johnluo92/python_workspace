class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def recoverBST(tree):
    
    return recoverBSTHelper(tree, None, float('-inf'), float('inf'))

def recoverBSTHelper(tree, parentNode, smallest, largest):
    if tree is None:
        return

    # if tree.left:
    #     if tree.left.value < smallest or tree.value > largest:
    #         tree.left.value, parentNode.value = parentNode.value, tree.value
    # if tree.right:
    #     if tree.right.value < smallest or tree.value > largest:
    #         tree.right.value, parentNode.value = parentNode.value, tree.value
    
    recoverBSTHelper(tree.left, tree, smallest, tree.value)
    if tree.value < smallest or tree.value > largest:
        tree.value, parentNode.value = parentNode.value, tree.value
    recoverBSTHelper(tree.right, tree, tree.value, largest)

def printmytree(tree):
    if tree:
        print(tree.value)
        printmytree(tree.left)
        printmytree(tree.right)

    #          10
    #      /       \
    #     5        15
    #    / \      /  \
    #   2   6    13  22
    #  /         / 
    # 1         16
    #          

    #          3                2   # expected
    #        /   \             / \
    #       1     4           1   4
    #            /               /
    #           2               3

# myTree = BST(10)
# myTree.left = BST(5)
# myTree.right = BST(15)
# myTree.right.right = BST(22)
# myTree.right.left = BST(13)
# myTree.right.left.left = BST(16)
# myTree.left.left = BST(2)
# myTree.left.right = BST(6)
# myTree.left.left.left = BST(1)

myTree = BST(3)
myTree.left = BST(1)
myTree.right = BST(4)
myTree.right.left = BST(2)
        
print(recoverBST(myTree))

printmytree(myTree)
