# O(n^2 time) | O(n) space
# n is the length of the input array
def maxSumIncreasingSubsequence(array):
    # Write your code here.
    dp = array[:]
    subsequenceMaxSum = array[0]
    subsequenceMaxSumIdx = 0
    indices = [None for element in array]
    for i in range(1, len(array)):
        maxSum = array[i]
        maxSumIdx = None
        for j in range(i):
            if array[i] > array[j]:
                currentMaxSum = dp[j] + array[i]
                if currentMaxSum > maxSum:
                    maxSum = currentMaxSum
                    maxSumIdx = j
        dp[i] = max(maxSum, array[i])
        if maxSum > array[i]:
            indices[i] = maxSumIdx
        if dp[i] > subsequenceMaxSum:
            subsequenceMaxSum = dp[i]
            subsequenceMaxSumIdx = i
    return [subsequenceMaxSum, reconstructSubsequence(array, indices, subsequenceMaxSumIdx)]

def reconstructSubsequence(array, indices, startIdx):
    subsequence = []
    while startIdx is not None:
        subsequence.append(array[startIdx])
        startIdx = indices[startIdx]
    return list(reversed(subsequence))
