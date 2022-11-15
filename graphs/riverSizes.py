# O(m * n) time | O(m * n) space
# m is the number of rows in the matrix
# n is the number of columns in the matrix
def riverSizes(matrix):
    # Write your code here.
    sizes = []
    visited = [[False for col in matrix[0]] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            size = dfs(matrix, row, col, visited)
            # size = dfsIterative(matrix, row, col, visited)
            # size = bfs(matrix, row, col, visited)
            if size != 0:
                sizes.append(size)
    return sizes

def dfs(matrix, row, col, visited):
    size = 0
    if matrix[row][col] == 1 and not visited[row][col]:
        size = 1
        visited[row][col] = True
        unvisitedNeighbors = getUnvisitedNeighbors(matrix, row, col, visited)
        for unvisitedNeighbor in unvisitedNeighbors:
            i, j = unvisitedNeighbor
            size += dfs(matrix, i, j, visited)
    return size

def dfsIterative(matrix, row, col, visited):
    size = 0
    if matrix[row][col] == 0:
        return size
    stack = [(row, col)]
    while stack:
        i, j = stack.pop()
        if not visited[i][j]:
            visited[i][j] = True
            size += 1
            unvisitedNeighbors = getUnvisitedNeighbors(matrix, i, j, visited)
            for unvisitedNeighbor in unvisitedNeighbors:
                stack.append(unvisitedNeighbor)
    return size

def bfs(matrix, row, col, visited):
    size = 0
    if matrix[row][col] == 0:
        return size
    queue = [(row, col)]
    while queue:
        i, j = queue.pop(0)
        if not visited[i][j]:
            visited[i][j] = True
            size += 1
            unvisitedNeighbors = getUnvisitedNeighbors(matrix, i, j, visited)
            for unvisitedNeighbor in unvisitedNeighbors:
                queue.append(unvisitedNeighbor)
    return size

def getUnvisitedNeighbors(matrix, row, col, visited):
    unvisitedNeighbors = []
    neighbors = [(row, col - 1), (row + 1, col), (row, col + 1), (row - 1, col)]
    for neighbor in neighbors:
        i, j = neighbor
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == 1 and not visited[i][j]:
            unvisitedNeighbors.append(neighbor)
    return unvisitedNeighbors
