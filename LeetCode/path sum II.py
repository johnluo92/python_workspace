# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        
        if not root:
            return []

        answer, array = [], []
        
        self.helper(root, target, answer, array)
        
        return answer
    
    def helper(self, root, target, answer, array):
        if not root.left and not root.right:
            if sum(array)+root.val == target:
                array.append(root.val)
                answer.append(array[:])
                array.pop()
                # print(answer, root.val)
            return
    
        array.append(root.val)
               
        if root.left:
            self.helper(root.left, target, answer, array)

        if root.right:
            self.helper(root.right, target, answer, array)
                
        array.pop()
        
        return