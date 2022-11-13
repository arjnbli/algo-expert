# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    # v is the number of vertices in the graph
    # e is the number of edges in the graph
    def breadthFirstSearch(self, array):
        # Write your code here.
        visited = set()
        queue = [self]
        while queue:
            vertex = queue.pop(0)
            array.append(vertex.name)
            for child in vertex.children:
                queue.append(child)
        return array
