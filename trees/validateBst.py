# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#O(n) time| O(d) space
#n is the number of nodes in the tree and d is the depth of the tree
def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree, float('-inf'), float('inf'))

def validateBstHelper(node, minVal, maxVal):
    if node is None:
        return True
    nodeIsValid = (minVal <= node.value < maxVal)
    leftSubtreeIsValid = validateBstHelper(node.left, minVal, node.value)
    rightSubtreeIsValid = validateBstHelper(node.right, node.value, maxVal)
    return nodeIsValid and leftSubtreeIsValid and rightSubtreeIsValid
    