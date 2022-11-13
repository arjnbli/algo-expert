class Vertex:
    def __init__(self, value, adjacent=None):
        self.value = value
        self.adjacent = [] if adjacent is None else adjacent

def visit(vertex):
    pass

# O(v + e) time | O(v + e) space
# v is the number of vertices in the graph
# e is the number of edges in the graph
def dfsIterative(startVertex):
    visited = set()
    stack = [startVertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited():
            visited.add(vertex)
            visit(vertex)
            for adjacentVertex in vertex.adjacent:
                if adjacentVertex not in visited:
                    stack.append(adjacentVertex)
    return 

# O(v + e) time | O(v + e) space
# v is the number of vertices in the graph
# e is the number of edges in the graph
def dfsRecursive(startVertex):
    return dfsRecursiveHelper(startVertex, set())

def dfsRecursiveHelper(vertex, visited):
    visit(vertex)
    visited.add(vertex)
    for adjacentVertex in vertex.adjacent:
        if adjacentVertex not in visited:
            dfsRecursiveHelper(adjacentVertex, visited)
    return
