# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    _, dim = binaryTreeDiameterHelper(tree, 0)
    return dim - 1

# O(n) time | O(d) space
# n is the length of the binary tree
# d is the depth of the binary tree
def binaryTreeDiameterHelper(node, dim):
    if node is None:
        return 0, 0
    lstLongestBranch, lstDim = binaryTreeDiameterHelper(node.left, dim)
    rstLongestBranch, rstDim = binaryTreeDiameterHelper(node.right, dim)
    longestBranchLength = max(lstLongestBranch, rstLongestBranch) + 1
    dim = max(dim, 1 + lstLongestBranch + rstLongestBranch, lstDim, rstDim)
    return longestBranchLength, dim
