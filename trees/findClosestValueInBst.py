# Average Case: O(log(n)) Time | O(1) Space
# Worst Case: O(n) Time | O(1) Space
def findClosestValueInBstIterative(tree, target):
    # Write your code here.
    closest = tree.value
    node = tree
    while node:
        if abs(target - node.value) < abs(target - closest):
            closest = node.value
        if node.value > target:
            node = node.left
        elif node.value < target:
            node = node.right
        else:
            break
    return closest

# Average Case: O(log(n)) Time | O(log(n)) Space
# Worst Case: O(n) Time | O(n) Space
def findClosestValueInBstRecursive(tree, target):
    # Write your code here.
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(node, target, closest):
    if node is None:
        return closest
    if abs(target - node.value) < abs(target - closest):
        closest = node.value
    if node.value > target:
        return findClosestValueInBstHelper(node.left, target, closest)
    elif node.value < target:
        return findClosestValueInBstHelper(node.right, target, closest)
    else:
        return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
