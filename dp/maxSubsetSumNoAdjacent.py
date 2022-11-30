# O(n^2) time | O(n) space
# n is the length of the input array
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    dp = array[:]
    dp[1] = max(dp[0], dp[1])
    for i in range(2, len(array)):
        dp[i] = max(dp[:i - 1]) + array[i]
    return max(dp)

# O(n) time | O(1) space
# n is the length of the input array
def maxSubsetSumNoAdjacent2(array):
    # Write your code here.
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    
    first = array[0]
    second = array[1]
    maxSubsetSum = max(first, second)
    for i in range(2, len(array)):
        dp = first + array[i]
        maxSubsetSum = max(maxSubsetSum, dp)
        first = max(first, second)
        second = dp
    return maxSubsetSum

# O(n) time | O(n) space
# n is the length of the input array
def maxSubsetSumNoAdjacent3(array):
    # Write your code here.
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    
    first = array[0]
    firstIdx = 0
    second = array[1]
    maxSubsetSum = max(first, second)
    maxSubsetSumIdx = 0 if first > second else 1
    indices = [None for element in array]
    for i in range(2, len(array)):
        dp = first + array[i]
        if dp > maxSubsetSum:
            maxSubsetSum = dp
            maxSubsetSumIdx = i
        indices[i] = firstIdx
        if second > first:
            first = second
            firstIdx = i - 1
        second = dp
    maxSubarrayNoAdjacent = reconstructSubarray(array, indices, maxSubsetSumIdx)
    print(maxSubarrayNoAdjacent)
    return sum(maxSubarrayNoAdjacent)

def reconstructSubarray(array, indices, startIdx):
    subarray = []
    while startIdx is not None:
        subarray.append(array[startIdx])
        startIdx = indices[startIdx]
    return list(reversed(subarray))
