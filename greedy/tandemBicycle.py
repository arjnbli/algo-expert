# O(n * log(n)) time | O(1) space
# n is the total number of elements in redShirtSpeeds and blueShirtSpeeds put together
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds.sort(reverse=True)
    else:
        blueShirtSpeeds.sort()
    r = 0
    b = 0
    total = 0
    while r < len(redShirtSpeeds) and b < len(blueShirtSpeeds):
        redShirtSpeed = redShirtSpeeds[r]
        blueShirtSpeed = blueShirtSpeeds[b]
        total += max(redShirtSpeed, blueShirtSpeed)
        r += 1
        b += 1
    return total

import heapq
# O(n * log(n)) time | O(1) space
# n is the total number of elements in redShirtSpeeds and blueShirtSpeeds put together
def tandemBicycle2(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    heapq.heapify(redShirtSpeeds)
    if fastest:
        for i in range(len(blueShirtSpeeds)):
            blueShirtSpeeds[i] *= -1
        heapq.heapify(blueShirtSpeeds)
    else:
        heapq.heapify(blueShirtSpeeds)

    totalSpeed = 0
    while redShirtSpeeds and blueShirtSpeeds:
        redShirtSpeed = heapq.heappop(redShirtSpeeds)
        blueShirtSpeed = heapq.heappop(blueShirtSpeeds)
        if blueShirtSpeed < 0:
            blueShirtSpeed *= -1
        totalSpeed += max(redShirtSpeed, blueShirtSpeed)
    return totalSpeed
