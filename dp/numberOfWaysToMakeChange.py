# O(n * d) | O(n)
# n is the target amount, d is the number of denominations at our disposal
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    dp = [0 for amount in range(n + 1)]
    dp[0] = 1
    for denom in denoms:
        for i in range(1, n + 1):
            if denom <= i:
                dp[i] += dp[i - denom] 
    return dp[n]
    