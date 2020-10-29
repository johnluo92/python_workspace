# Definition for a binary tree node.

"""
See if the tree is balanced or not meaning each node's left and right's depth shouldn't be more than 1 distance apart.

First solution is a lot faster since it calculates the validity as each depth is traversed, whereas the second solution recurisively validates each node to see if it is a balanced tree or not by the valiate function with height function called on each node.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        depth = 0
        balanced, _ = self.getDepth(root, depth)
        print(balanced)
        return balanced
    
    def getDepth(self, root, depth):
        if not root:
            return True, depth-1
        
        leftBalanced, left = self.getDepth(root.left, depth+1)
        rightBalanced, right = self.getDepth(root.right, depth+1)

        maxDepth = max(left, right)
        balanced = bool(abs(left-right) <= 1)
        balanced = all([balanced, leftBalanced, rightBalanced])
        
        return balanced, maxDepth

# ------------------------------------------------------

"""
                           1
                         /   \
                        2     5
                       /       \
                      3         6
                     /           \
                    4             7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if not root:
            return True

        balanced = self.validate(root)
        print(balanced)
        return balanced

    def validate(self, root):
        if not root:
            return True

        validate_left = self.validate(root.left)
        validate_right = self.validate(root.right)

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        balanced = bool(abs(left_height - right_height) <= 1)
        validated = bool(validate_left and validate_right and balanced)

        print(left_height, right_height, validated, root.val)

        return validated
    
    def getHeight(self, root, depth = None):
        if depth is None:
            depth = 0
        if not root:
            return depth
            
        left = self.getHeight(root.left, depth + 1)
        right = self.getHeight(root.right, depth + 1)
        
        return max(left, right)



myTree = TreeNode(1)
myTree.left = TreeNode(2)
myTree.left.left = TreeNode(3)
myTree.left.left.left = TreeNode(4)
myTree.right = TreeNode(5)
myTree.right.right = TreeNode(6)
myTree.right.right.right = TreeNode(7)


# myTree = TreeNode(9)
# myTree.left = TreeNode(8)
# myTree.right = TreeNode(3)
# myTree.right.right = TreeNode(3)
# myTree.right.left = TreeNode(3)


Solution().isBalanced(myTree)