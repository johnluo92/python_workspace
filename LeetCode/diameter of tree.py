# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        ans = self.getDiameterHelper(root)
        print(ans)
        return ans
        
    def getDiameterHelper(self, root):
        if root is None:
            return 0
        
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        left_diameter = self.getDiameterHelper(root.left)
        right_diameter = self.getDiameterHelper(root.right)
        
        final_diameter = max(left_height + right_height, max(left_diameter, right_diameter))
        return final_diameter
    
    def getHeight(self, root, depth = None):
        if depth is None:
            depth = 0
        if root is None:
            return depth
        
        left = self.getHeight(root.left, depth+1)
        right = self.getHeight(root.right, depth+1)
        
        return max(left, right)

"""

                            2
                           / \
                          /   \
                         /     \
                        1       3
                       / \  
                      0   7 
                     /   / \    
                    2   1   0   
                           / \
                          7   3
                         / \  
                        0   7 
                       /   / \    
                      2   1   0   
                             /
                            7
"""
myTree = TreeNode(1)
myTree.left = TreeNode(2)
# myTree.left.left = TreeNode(4)
# myTree.left.right = TreeNode(5)
myTree.right = TreeNode(3)

Solution().diameterOfBinaryTree(myTree)