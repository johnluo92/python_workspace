# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = ''
        return self.serialize_helper(root, string)
        
    def serialize_helper(self, root, string):
        if root is None:
            string += 'None,'
        else:
            string = string + str(root.val) + ',' #separator very important!
            string = self.serialize_helper(root.left, string)
            string = self.serialize_helper(root.right, string)
        return string

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #data is the string version of our tree
        #serialized with str concatenated values with ',' as
        #separators
        arrayOfVals = data.split(',')
        return self.deserialize_helper(arrayOfVals)
    
    def deserialize_helper(self, arrayOfVals):
        # print(arrayOfVals)
        if arrayOfVals[0] == 'None':
            arrayOfVals.pop(0)
            return None
        else:
            root = TreeNode(arrayOfVals[0])
            arrayOfVals.pop(0)
            root.left = self.deserialize_helper(arrayOfVals)
            root.right = self.deserialize_helper(arrayOfVals)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))