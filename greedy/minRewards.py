# O(n) time | O(n) space
# n is the length of the input array
def minRewards(scores):
    # Write your code here.
    if len(scores) == 1:
        return 1
        
    valleyIndices = []
    if scores[0] < scores[1]:
        valleyIndices.append(0)
    if scores[-1] < scores[-2]:
        valleyIndices.append(len(scores) - 1)
    for i in range(1, len(scores) - 1):
        if scores[i - 1] > scores[i] and scores[i] < scores[i + 1]:
            valleyIndices.append(i)

    rewards = [1 for score in scores]
    for idx in valleyIndices:
        leftRewards = rewards[idx] + 1
        left = idx - 1
        while left >= 0 and scores[left + 1] < scores[left]:
            rewards[left] = max(rewards[left], leftRewards)
            leftRewards += 1
            left -= 1

        rightRewards = rewards[idx] + 1
        right = idx + 1
        while right < len(scores) and scores[right - 1] < scores[right]:
            rewards[right] = max(rewards[right], rightRewards)
            rightRewards += 1
            right += 1   
    return sum(rewards)
