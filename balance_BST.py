# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        holder_list = []
        
        def in_order_list(root):
            if root:
                in_order_list(root.left)
                holder_list.append(root.val)
                in_order_list(root.right)
            return holder_list # this changes the list
   
        '''The above is a function inside the function balanceBST. This is not a class function but just a helper function it has one param which is the root, recursively called to traverse it. It outputs an array which it takes from the outter function, accessing and manipulating it to give the desdired output based on the input root'''
        
        '''this is an in function call, which does not require self, meaning it is not a class method, it is merely a inner function method used to help the main function output/return stuff. Here it is called on the root, which is then evaluated the way the instructions are given in its function'''
        in_order_list(root)
        
        '''this is another function within the parent function, another helper function if you will. Its job is to take the list another helper method just manipulated and is going to use it to generate a tree, or individual nodes using the class TreeNode by creating new TreeNode objects tying them to each other in line 39. It is recurisvely called, after initializing the root node, it will initialize its left and right child nodes.
'''
        def BST_maker_helper(holder_list):
            if not holder_list:
                return
            mid = len(holder_list) // 2
            root = TreeNode(holder_list[mid])
            root.left = BST_maker_helper(holder_list[:mid])
            root.right = BST_maker_helper(holder_list[mid + 1:])
            return root

        '''here the above method is called by the method balanceBST, which is a class function. It actually calls the method BST_maker_helper on the the list in_order_list method manipulated using the original root passed down by the calling of balanceBST method.
'''
        return BST_maker_helper(holder_list)
    
    
    # balanceBST(root) -> in_order_list(root) -> #list# -> BST_maker_helper(list)