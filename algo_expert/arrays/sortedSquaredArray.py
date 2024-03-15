# Approach: Brute Force
# Time: O(n * log(n))
# Space: O(n)
# n is the length of array
def sortedSquaredArray(array):
    result = [num**2 for num in array]
    result.sort()
    return result


# Approach: Two Pointers, Optimal
# Time: O(n)
# Space: O(n)
# n is the length of array
def sortedSquaredArray(array):
    result = []
    start, end = 0, len(array) - 1
    while start <= end:
        if abs(array[start]) <= abs(array[end]):
            result.append(array[end] ** 2)
            end -= 1
        else:
            result.append(array[start] ** 2)
            start += 1
    return list(reversed(result))
