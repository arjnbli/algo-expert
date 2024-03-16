# Approach: Double For Loop, Optimal
# Time: O(r * c)
# Space: O(r * c)
# r is the number of rows in the matrix
# c is the number of columns in the matrix
def transposeMatrix(matrix):
    transpose = []
    for col in range(len(matrix[0])):
        transposedRow = []
        for row in range(len(matrix)):
            transposedRow.append(matrix[row][col])
        transpose.append(transposedRow)
    return transpose
