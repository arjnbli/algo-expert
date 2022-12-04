# O(k * n) time | O(k * n) space
# k is the max number of allowed transactions
# n is the length of the prices array
def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    if len(prices) == 0 or k == 0:
        return 0
    dp = [[0 for price in prices] for i in range(k + 1)]
    for i in range(1, k + 1):
        prevMax = float('-inf')
        for j in range(1, len(prices)):
            prevMax = max(prevMax, dp[i - 1][j - 1] - prices[j - 1])
            dp[i][j] = max(
                dp[i][j - 1],
                dp[i - 1][j],
                prices[j] + prevMax
            )
    return dp[-1][-1]

# O(k * n) time | O(n) space
# k is the max number of allowed transactions
# n is the length of the prices array
def maxProfitWithKTransactions2(prices, k):
    # Write your code here.
    if len(prices) == 0 or k == 0:
        return 0
    previous = [0 for price in prices]
    for i in range(k):
        dp = [0 for price in prices]
        prevMax = float('-inf')
        for j in range(1, len(prices)):
            prevMax = max(prevMax, previous[j - 1] - prices[j - 1])
            dp[j] = max(
                dp[j - 1],
                previous[j],
                prices[j] + prevMax
            )
        previous = dp
    return dp[-1]
