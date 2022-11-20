import heapq

# O(n * log(n)) time | O(n) space
def laptopRentals(times):
    # Write your code here.
    if len(times) == 0:
        return 0
    times.sort()
    heap = [(times[0][1], times[0][0])]
    for i in range(1, len(times)):
        startTime, endTime = times[i]
        heapEndTime, heapStartTime = heap[0]
        if startTime >= heapEndTime:
            heapq.heappop(heap)
        heapq.heappush(heap, (endTime, startTime))
    return len(heap)