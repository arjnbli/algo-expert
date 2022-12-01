# O(n^2) time | O(n) space
# n is the length of the input array
def longestIncreasingSubsequence(array):
    # Write your code here.
    longestSubsequenceStartIdx = 0
    longestSubsequenceLength = 1
    dp = [1 for element in array]
    indices = [None for element in array]
    for i in range(1, len(array)):
        longest = dp[i]
        longestIdx = indices[i]
        for j in range(i):
            if array[i] > array[j]:
                subsequenceLength = 1 + dp[j]
                if subsequenceLength > longest:
                    longest = subsequenceLength
                    longestIdx = j
        dp[i] = longest
        indices[i] = longestIdx
        if dp[i] > longestSubsequenceLength:
            longestSubsequenceLength = dp[i]
            longestSubsequenceStartIdx = i
    return buildSubsequence(array, indices, longestSubsequenceStartIdx)

def buildSubsequence(array, indices, startIdx):
    subsequence = []
    while startIdx is not None:
        subsequence.append(array[startIdx])
        startIdx = indices[startIdx]
    return list(reversed(subsequence))
