def minHeightBst(array):
    sentinel = minHeightBstHelper(BST(float('-inf')), array, 0, len(array) - 1)
    return sentinel.right

# O(n * log(n)) time | O(n) space
# n is the length of the input array
def minHeightBstHelper(tree, array, startIdx, endIdx):
    if startIdx == endIdx:
        tree.insert(array[startIdx])
        return tree

    if startIdx > endIdx:
        return tree
    
    middle = (startIdx + endIdx) // 2
    tree.insert(array[middle])
    minHeightBstHelper(tree, array, startIdx, middle - 1)
    minHeightBstHelper(tree, array, middle + 1, endIdx)
    return tree

# O(n) time | O(n) space
# n is the length of the input array
def minHeightBstHelper2(tree, array, startIdx, endIdx):
    if startIdx == endIdx:
        tree.insert(array[startIdx])
        return tree
    if startIdx > endIdx:
        return tree
    middle = (startIdx + endIdx) // 2
    if array[middle] < tree.value:
        tree.left = BST(array[middle])
        root = tree.left
    else:
        tree.right = BST(array[middle])
        root = tree.right

    minHeightBstHelper(root, array, startIdx, middle - 1)
    minHeightBstHelper(root, array, middle + 1, endIdx)
    return tree

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
