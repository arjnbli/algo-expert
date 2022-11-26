# O(n * log (n)) time | O(1) space
# n is the total number of elements 
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    if redShirtHeights[0] > blueShirtHeights[0]:
        backRow = redShirtHeights
        frontRow = blueShirtHeights
    elif redShirtHeights[0] < blueShirtHeights[0]:
        backRow = blueShirtHeights
        frontRow = redShirtHeights
    else:
        return False
    
    back = 1
    front = 1
    while back < len(backRow) and front < len(frontRow):
        if frontRow[front] >= backRow[back]:
            return False
        back += 1   
        front += 1
    
    return True

import heapq

# O(n * log (n)) time | O(1) space
# n is the total number of elements 
def classPhotos2(redShirtHeights, blueShirtHeights):
    # Write your code here.
    heapq.heapify(redShirtHeights)
    heapq.heapify(blueShirtHeights)
    if redShirtHeights[0] > blueShirtHeights[0]:
        backRow = redShirtHeights
        frontRow = blueShirtHeights
    elif redShirtHeights[0] < blueShirtHeights[0]:
        backRow = blueShirtHeights
        frontRow = redShirtHeights
    else:
        return False
    while backRow and frontRow:
        backRowStudent = heapq.heappop(backRow)
        frontRowStudent = heapq.heappop(frontRow)
        if backRowStudent <= frontRowStudent:
            return False
    return True
    