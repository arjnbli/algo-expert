import heapq

# O(n * k) time | O(n + k) space
# n is the number of elements in input array
# k is the factor by which input array is 'k-sorted'
def sortKSortedArray1(array, k):
    # Write your code here.
    if len(array) == 0:
        return array
    sortedArray = []
    for i in range(len(array) - 1):
        candidates = [(array[i], i) for i in range(i,min(len(array),i + k + 1))]
        heapq.heapify(candidates)
        val, idx = heapq.heappop(candidates)
        array[i], array[idx] = array[idx], array[i]
        sortedArray.append(val)
    sortedArray.append(array[-1])
    return sortedArray

# O(n * log(k)) time | O(n + k) space
# n is the number of elements in input array
# k is the factor by which input array is 'k-sorted'
def sortKSortedArray2(array, k):
    # Write your code here.
    sortedArray = []
    heap = array[: k + 1]
    heapq.heapify(heap)
    next = k + 1
    while heap:
        sortedValue = heapq.heappop(heap)
        sortedArray.append(sortedValue)
        if next < len(array):
            heapq.heappush(heap, array[next])
            next += 1
    return sortedArray

# O(n * log(k)) time | O(k) space
# n is the number of elements in input array
# k is the factor by which input array is 'k-sorted'
def sortKSortedArray3(array, k):
    # Write your code here.
    idx = 0
    heap = array[: k + 1]
    heapq.heapify(heap)
    next = k + 1
    while heap:
        sortedVal = heapq.heappop(heap)
        array[idx] = sortedVal
        idx += 1
        if next < len(array):
            heapq.heappush(heap, array[next])
            next += 1
    return array
