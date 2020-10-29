# 199 Binary Ttree Right Side View

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        depthStack = {}
        ans = []
        
        self.depthStackFiller(root, depthStack, 0)
        
        for depth in depthStack:
            ans.append(depthStack[depth][-1])
        print('depthStack: ', depthStack)
        return ans
    
    def depthStackFiller(self, root, stack, depth):
        if not root:
            return
        
        if depth not in stack:
            stack[depth] = [root.val]
        else:
            stack[depth].append(root.val)
        self.depthStackFiller(root.left, stack, depth+1)
        self.depthStackFiller(root.right, stack, depth+1)
            
myTree = TreeNode(1)
myTree.left = TreeNode(2)
myTree.left.right = TreeNode(5)
myTree.left.right.left = TreeNode(3.5)
myTree.right = TreeNode(3)
myTree.right.right = TreeNode(4)

'''
			    1
			/   	\
		   2		 3
		    \   	  \
			 5         4
			/
		   3.5

1
2, 3
5, 4
3.5

'''

ans = Solution()
print(ans.rightSideView(myTree))