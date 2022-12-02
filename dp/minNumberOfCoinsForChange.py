# O(n * d) time | O(n) space
# n is the target amount
# d is the number of denominations available
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    dp = [float('inf') for i in range(n + 1)]
    dp[0] = 0
    for denom in denoms:
        for i in range(1, n + 1):
            if denom <= i:
                dp[i] = min(dp[i], 1 + dp[i - denom])
    return dp[-1] if dp[-1] != float('inf') else -1
