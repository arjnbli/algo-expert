import heapq

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
