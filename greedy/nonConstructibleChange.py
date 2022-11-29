# O(n * log(n)) time | O(1) space
def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    constructible = 0
    for coin in coins:
        if coin > constructible + 1:
            break
        constructible += coin
    return constructible + 1
    