# O(n) time | O(d) space
# n is the number of nodes in the binary tree
# d is the depth of the binary tree
def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
        return tree
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    tree.left, tree.right = tree.right, tree.left
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
