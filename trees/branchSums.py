# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    # Write your code here.
    if root is None:
        return 0
    return branchSumsHelper(root, 0, [])
    
# O(n) time | O(n) space
# n is the number of nodes in the tree
def branchSumsHelper(node, runningSum, sumsArray):
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sumsArray.append(newRunningSum)
    if node.left:
        branchSumsHelper(node.left, newRunningSum, sumsArray)
    if node.right:
        branchSumsHelper(node.right, newRunningSum, sumsArray)
    return sumsArray