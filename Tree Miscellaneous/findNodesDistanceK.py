# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findNodesDistanceK(tree, target, k):
    # Write your code here.
    ancestors, children = {}, {}
    mapRelationships(tree, ancestors, children) #manipulates a dictionary containing nodes and their parent

    return getKDistancedNodes(target, k, ancestors, children)

def mapRelationships(tree, ancestors, children, ancestor = None):
    if tree is None:
        return
    ancestors[tree.value] = ancestor

    if ancestor not in children:
        children[ancestor] = []
    children[ancestor].append(tree.value)

    mapRelationships(tree.left, ancestors, children, tree.value)
    mapRelationships(tree.right, ancestors, children, tree.value)

def getKDistancedNodes(target, k, ancestors, children):
    answer = set()
    if ancestors[target] is not None:
        goUp(target, k, ancestors, children, answer, target)
    goDown(target, k, children, answer)
    return list(answer)

def goUp(currVal, k, ancestors, children, answer, originVal = None):
    if currVal is None:
        return

    if k == 0:
        answer.add(currVal)
        return

    # if ancestors[currVal] is None:
    if currVal in children:
        for nodeVal in children[currVal]:
            if nodeVal != originVal:
                goDown(nodeVal, k-1, children, answer)

    goUp(ancestors[currVal], k-1, ancestors, children, answer, currVal)

def goDown(currVal, k, children, answer):
    if currVal is None:
        return

    if k == 0:
        answer.add(currVal)
        return

    if currVal in children:
        for nodeVal in children[currVal]:
            goDown(nodeVal, k-1, children, answer)