# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.

    if isAncestor(nodeOne, nodeTwo):
        return isAncestor(nodeTwo, nodeThree)
    elif isAncestor(nodeThree, nodeTwo):
        return isAncestor(nodeTwo, nodeOne)
        
    return False

def isAncestor(tree, descendant):
    if not tree:
        return False

    if tree == descendant:
        return True

    return isAncestor(tree.left, descendant) or isAncestor(tree.right, descendant)