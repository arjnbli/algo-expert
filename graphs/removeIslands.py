class IslandInfo:
    def __init__(self, matrix):
        self.matrix = matrix
        self.isIsland = True
        self.coords = []
    
    def addCoord(self, row, col):
        self.coords.append((row, col))
    
    def removeIsland(self):
        if self.isIsland and len(self.coords) != 0:
            for coord in self.coords:
                row, col = coord
                self.matrix[row][col] = 0

# O(m * n) time | O(m * n) space
# m is the number of rows in the matrix
# n is the number of columns in the matrix
def removeIslands(matrix):
    visited = [[False for col in matrix[0]] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            # info = dfs(matrix, row, col, visited, IslandInfo(matrix))
            # info = dfsIterative(matrix, row, col, visited)
            info = bfs(matrix, row, col, visited)
            info.removeIsland()
    return matrix

def dfs(matrix, row, col, visited, islandInfo):
    if matrix[row][col] == 0:
        islandInfo.isIsland = False
        return islandInfo
    if not visited[row][col]:
        visited[row][col] = True
        if row == 0 or row == (len(matrix) - 1) or col == 0 or col == (len(matrix[0]) - 1):
            islandInfo.isIsland = False
        islandInfo.addCoord(row, col)
        neighbors = getNeighbors(matrix, row, col)
        for neighbor in neighbors:
            i, j = neighbor
            dfs(matrix, i, j, visited, islandInfo)
    return islandInfo

def dfsIterative(matrix, row, col, visited):
    info = IslandInfo(matrix)
    if matrix[row][col] == 0:
        info.isIsland = False
        return info
    stack = [(row, col)]
    while stack:
        i, j = stack.pop()
        if not visited[i][j]:
            visited[i][j] = True
            if i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[0]) - 1:
                info.isIsland = False
            info.addCoord(i, j)
            neighbors = getNeighbors(matrix, i, j)
            for neighbor in neighbors:
                stack.append(neighbor)
    return info

def bfs(matrix, row, col, visited):
    info = IslandInfo(matrix)
    if matrix[row][col] == 0:
        info.isIsland = False
        return info
    queue = [(row, col)]
    while queue:
        i, j = queue.pop(0)
        if not visited[i][j]:
            visited[i][j] = True
            if i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[0]) - 1:
                info.isIsland = False
            info.addCoord(i, j)
            neighbors = getNeighbors(matrix, i, j)
            for neighbor in neighbors:
                queue.append(neighbor)
    return info

def getNeighbors(matrix, row, col):
    neighbors = []
    potentialNeighbors = [(row, col - 1), (row + 1, col), (row, col + 1), (row - 1, col)]
    for potentialNeighbor in potentialNeighbors:
        i, j = potentialNeighbor
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == 1:
            neighbors.append(potentialNeighbor)
    return neighbors

