import heapq
# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.maxHeap = []
        self.minHeap = []

    # O(log(n)) time | O(1) space per operation
    # O(log(n)) time | O(n) space for all n operations
    # n is the length of the numbers in the stream seen so far
    def insert(self, number):
        # Write your code here.
        if len(self.maxHeap) == 0 and len(self.minHeap) == 0:
            heapq.heappush(self.maxHeap, -number)
            self.median = number
            return
            
        if number > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, number)
        else:
            heapq.heappush(self.maxHeap, -number)
        
        self.rebalance()
        self.updateMedian()

    def rebalance(self):
        if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                maxHeapValue = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -maxHeapValue)
            else:
                minHeapValue = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -minHeapValue)

    def updateMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            self.median = (self.minHeap[0] - self.maxHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            self.median = self.minHeap[0]
        else:
            self.median = -self.maxHeap[0]

    def getMedian(self):
        return self.median
