# validate binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def validate_tree_node(nodelist, seen = set()):

    for node in nodelist:
        if node in seen:
            return False
        seen.add(node)

    return True

# n1 = TreeNode(1);
# n2 = TreeNode(2);
# n3 = TreeNode(3);
# n4 = TreeNode(4);

# n1.left = n2;
# n1.right = n3;
# n3.left = n4;

# Input = [n4, n2, n3, n1]
# Output: true

# print(validate_tree_node(Input))

      #    1
      #  ↙  ↘
      # 2    3
      #  ↘  ↙
      #   4

n1 = TreeNode(1);
n2 = TreeNode(2);
n3 = TreeNode(3);
n4 = TreeNode(4);

n1.left = n2;
n1.right = n3;
n2.right = n4;
n3.left = n4;

Input: [n2, n3, n4, n1]
# Output: false

print(validate_tree_node(Input))