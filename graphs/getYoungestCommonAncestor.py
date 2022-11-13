# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(d) time | O(1) space
# d is depth of the tree/graph
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    descendantOneLevel = getVertexLevel(descendantOne)
    descendantTwoLevel = getVertexLevel(descendantTwo)
    if descendantOneLevel > descendantTwoLevel:
        descendantOne = traverseUpwards(descendantOne, descendantOneLevel - descendantTwoLevel)
    else:
        descendantTwo = traverseUpwards(descendantTwo, descendantTwoLevel - descendantOneLevel)
    if descendantOne == descendantTwo:
        return descendantOne
    while descendantOne.ancestor != descendantTwo.ancestor:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
    return descendantOne.ancestor

def getVertexLevel(vertex):
    level = 0
    while vertex.ancestor:
        level += 1
        vertex = vertex.ancestor
    return level

def traverseUpwards(vertex, levels):
    for i in range(levels):
        vertex = vertex.ancestor
    return vertex
