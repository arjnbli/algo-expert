# O(n) time | O(1) space
# n is the length of the input array
def kadanesAlgorithm(array):
    # Write your code here.
    maxSubsetSum = array[0]
    dp = array[0]
    for i in range(1, len(array)):
        dp = max(dp + array[i], array[i])
        maxSubsetSum = max(maxSubsetSum, dp)
    return maxSubsetSum

# O(n) time | O(n) space
# n is the length of the input array
def kadanesAlgorithm2(array):
    # Write your code here.
    dp = [array[0] for elem in array]
    for i in range(1, len(array)):
        dp[i] = max(dp[i - 1] + array[i], array[i])
    return max(dp)

# O(n) time | O(1) space
# n is the length of the input array
def kadanesAlgorithm(array):
    # Write your code here.
    maxSubsetSum = array[0]
    maxSubsetSumIdx = [0, 0]
    startIdx = 0
    endIdx = 0
    dp = array[0]
    for i in range(1, len(array)):
        if dp + array[i] > array[i]:
            dp += array[i]
            endIdx = i
        else:
            dp = array[i]
            startIdx = i
            endIdx = i
        if dp > maxSubsetSum:
            maxSubsetSum = dp
            maxSubsetSumIdx = [startIdx, endIdx]
    print(array[maxSubsetSumIdx[0]: maxSubsetSumIdx[1] + 1])
    return sum(array[maxSubsetSumIdx[0]: maxSubsetSumIdx[1] + 1])

# O(n) time | O(1) space
# n is the length of the input array
def kadanesAlgorithm4(array):
    # Write your code here.
    maxSubsetSum = float('-inf')
    for i in range(len(array)):
        sum = 0
        for j in range(i, len(array)):
            sum += array[j]
            maxSubsetSum = max(maxSubsetSum, sum)
    return maxSubsetSum