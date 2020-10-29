# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        found = self.helper(root, 0, target)
        
        return found
    
    def helper(self, root, runningSum, target):
        if not root.left and not root.right:
            return runningSum+root.val == target
    
        runningSum += root.val
               
        if root.left:
            found = self.helper(root.left, runningSum, target)
            if found: return found
        if root.right:
            found = self.helper(root.right, runningSum, target)
            if found: return found
               
        return False