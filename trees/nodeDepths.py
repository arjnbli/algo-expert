def nodeDepths(root):
    # Write your code here.
    return nodeDepthsHelper(root, 0)

# O(n) time | O(d) space
# n is the number of nodes in the binary tree and d is the depth of the binary tree
def nodeDepthsHelper(node, depth):
    if node is None:
        return 0
    return depth + nodeDepthsHelper(node.left, depth + 1) + nodeDepthsHelper(node.right, depth + 1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
