# Approach: One-pass, Optimal
# Time: O(n)
# Space: O(1)
# n is the length of array
def isValidSubsequence(array, sequence):
    i = 0
    for num in array:
        if num == sequence[i]:
            i += 1
        if i == len(sequence):
            return True
    return False
