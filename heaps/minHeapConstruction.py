class MinHeap:
    def __init__(self, array, type='min'):
        self.comparisonFunc = self.minFunc if type == 'min' else self.maxFunc
        self.heap = self.heapify(array)
    
    # O(log(n)) time | O(1) space
    # n is the number of elements in the heap
    def siftUp(self, heap, idx):
        while idx > 0:
            parentIdx = (idx - 1) // 2
            if parentIdx < 0 or not self.comparisonFunc(heap[idx], heap[parentIdx]):
                return
            self.swap(heap, idx, parentIdx)
            idx = parentIdx

    # O(log(n)) time | O(1) space
    # n is the number of elements in the heap
    def siftDown(self, heap, idx):
        while idx < len(heap):
            minChildIdx = 2 * idx + 1
            if minChildIdx >= len(heap):
                return
            rightChildIdx = 2 * idx + 2
            if rightChildIdx < len(heap):
                minChildIdx = rightChildIdx if self.comparisonFunc(heap[rightChildIdx], heap[minChildIdx]) else minChildIdx
            if self.comparisonFunc(heap[minChildIdx], heap[idx]):
                self.swap(heap, minChildIdx, idx)
                idx = minChildIdx
            else:
                return

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap) - 1)

    def remove(self):
        if len(self.heap) == 0:
            return None
        self.swap(self.heap, 0, len(self.heap) - 1)
        heapValue = self.heap.pop()
        self.siftDown(self.heap, 0)
        return heapValue


    # O(log(n)) time | O(1) space
    # n is the length of the input array
    def heapify(self, array):
        for idx in reversed(range(len(array))):
            self.siftDown(array, idx)
        return array

    # O(1) time | O(1) space
    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    # O(1) time | O(1) space
    def swap(self, heap, idx1, idx2):
        heap[idx1], heap[idx2] =  heap[idx2], heap[idx1]

    # O(1) time | O(1) space
    def minFunc(self, a, b):
        return a < b

    # O(1) time | O(1) space
    def maxFunc(self, a, b):
        return a > b
    
        
if __name__ == '__main__':
    array = [1, -1, 0]
    heap = MinHeap(array)
    print(heap.heap)