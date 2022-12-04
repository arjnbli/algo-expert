# O(w * h) time | O(w * h) space
# w is the width of the rectangular grid
# h is the height of the rectangular grid
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    dp = [[1 for j in range(width)] for i in range(height)]
    for i in range(1, height):
        for j in range(1, width):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[-1][-1]

# O(w * h) time | O(w) space
# w is the width of the rectangular grid
# h is the height of the rectangular grid
def numberOfWaysToTraverseGraph2(width, height):
    # Write your code here.
    previous = [1 for j in range(width)]
    for i in range(1, height):
        dp = [1 for j in range(width)]
        for j in range(1, width):
            dp[j] = dp[j - 1] + previous[j]
        previous = dp
    return previous[-1]
