# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = -float('inf')
        
        self.get_path_sum(root)
        
        return self.max_sum
    
    def get_path_sum(self, root):
        
        if not root:
            return 0
        
        left = self.get_path_sum(root.left)
        right = self.get_path_sum(root.right)
        
        self.max_sum = max(self.max_sum, root.val + left + right)
        
        return max(0, root.val + max(left, right))