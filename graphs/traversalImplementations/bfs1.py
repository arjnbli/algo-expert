class Vertex:
    def __init__(self, value, adjacent=None):
        self.value = value
        self.adjacent = [] if adjacent is None else adjacent

def visit(vertex):
    pass

# O(v + e) time | O(v + e) space
# v is the number of vertices in the graph
# e is the number of edges in the graph 
def bfs(startVertex):
    visited = set()
    queue = [startVertex]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            visit(vertex)
            for adjacentVertex in vertex.adjacent:
                if adjacentVertex not in visited:
                    queue.append(adjacentVertex)
    return 
