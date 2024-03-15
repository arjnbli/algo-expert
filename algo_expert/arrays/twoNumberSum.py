# Approach: Brute Foce
# Time: O(n^2)
# Space: O(1)
# n is the length of array
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []


# Approach: Sort + Two Pointers
# Time: O(n * log(n))
# Space: O(1)
# n is the length of array
def twoNumberSum(array, targetSum):
    array.sort()
    start = 0
    end = len(array) - 1
    while start < end:
        if array[start] + array[end] == targetSum:
            return [array[start], array[end]]
        elif array[start] + array[end] < targetSum:
            start += 1
        else:
            end -= 1
    return []


# Approach: Hash Set + One Pass
# Time: O(n)
# Space: O(n)
# n is the length of array
def twoNumberSum(array, targetSum):
    seen = set()
    for num in array:
        if targetSum - num in seen:
            return [num, targetSum - num]
        seen.add(num)
    return []
