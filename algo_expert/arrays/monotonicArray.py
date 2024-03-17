# Approach: One-pass, Optimal
# Time: O(n)
# Space: O(1)
# n is the length of array
def isMonotonic(array):
    isNonIncreasing = True
    isNonDecreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            isNonIncreasing = False
        if array[i] < array[i - 1]:
            isNonDecreasing = False
    return isNonIncreasing or isNonDecreasing
