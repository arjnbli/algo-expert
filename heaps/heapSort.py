# O(n * log(n)) time | O(1) space
# n is the length of the input array
def heapSort(array):
    # Write your code here.
    sortedArray = maxHeapify(array)
    for i in reversed(range(1, len(array))):
        sortedArray[0], sortedArray[i] = sortedArray[i], sortedArray[0]
        siftDown(array, i - 1, 0)
    return sortedArray

def siftDown(array, endIdx, idx):
    while idx <= endIdx:
        maxChildIdx = 2 * idx + 1
        if maxChildIdx > endIdx:
            return
        rightChildIdx = 2 * idx + 2
        if rightChildIdx <= endIdx:
            maxChildIdx = maxChildIdx if array[maxChildIdx] > array[rightChildIdx] else rightChildIdx
        if array[idx] >= array[maxChildIdx]:
            return
        array[idx], array[maxChildIdx] = array[maxChildIdx], array[idx]
        idx = maxChildIdx

def maxHeapify(array):
    lastParentIdx = (len(array) - 1) // 2
    for i in reversed(range(lastParentIdx + 1)):
        siftDown(array, len(array) - 1, i)
    return array
