# https://leetcode.com/problems/longest-univalue-path/

# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

# The length of the path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root):
        
        self.max_unival_path = 0
        
        self.get_longest_uni(root)
        return self.max_unival_path
    
    def get_longest_uni(self, root):
        
        if not root:
            return 0
        
        leftmax, rightmax, center = 0, 0, 0
        
        left_path = self.get_longest_uni(root.left)
        if root.left:
            if root.val == root.left.val:
                leftmax = left_path + 1
        
        right_path = self.get_longest_uni(root.right)
        if root.right:
            if root.val == root.right.val:
                rightmax = right_path + 1
                
        if root.left and root.right:
            if root.left.val == root.val == root.right.val:
                center = 2 + left_path + right_path
                
        self.max_unival_path = max(self.max_unival_path, center, leftmax, rightmax)
        
        return max(leftmax, rightmax)