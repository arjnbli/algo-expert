import heapq

# O(n * log(n)) time | O(1) space
def minimumWaitingTime(queries):
    # Write your code here.
    heapq.heapify(queries)
    waitingTime = 0
    currWaitingTime = 0
    while queries:
        waitingTime += currWaitingTime
        queryExecutionTime = heapq.heappop(queries)
        currWaitingTime += queryExecutionTime
    return waitingTime

# O(n * log(n)) time | O(1) space
def minimumWaitingTime2(queries):
    # Write your code here.
    queries.sort()
    currentWaitingTime = queries[0]
    totalWaitingTime = 0
    for i in range(1, len(queries)):
        totalWaitingTime += currentWaitingTime
        currentWaitingTime += queries[i]
    return totalWaitingTime
    