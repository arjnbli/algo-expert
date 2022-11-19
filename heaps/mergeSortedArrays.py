import heapq

# O(n * log(k) + k) time | O(n + k) space
# n is the total number of elements in all the arrays
# k is the number of sorted array to be merged
def mergeSortedArrays(arrays):
    # Write your code here.
    arrayPointer = [1 for array in arrays]
    heap = [(array[0], idx) for idx, array in enumerate(arrays)]
    heapq.heapify(heap)
    mergedArray = []
    while heap:
        arrayVal, arrayId = heapq.heappop(heap)
        array = arrays[arrayId]
        pointer = arrayPointer[arrayId]
        if pointer < len(array):
            heapq.heappush(heap, (array[pointer], arrayId))
            arrayPointer[arrayId] += 1
        mergedArray.append(arrayVal)
    return mergedArray
