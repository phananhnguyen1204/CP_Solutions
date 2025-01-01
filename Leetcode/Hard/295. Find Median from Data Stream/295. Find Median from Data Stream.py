from heapq import heappush, heappop
class MedianFinder:
    # [4, 3, 2, 1]
    #
    # min_heap = [3, 4]
    # max_heap = [2, 1]

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)
        heappush(self.min_heap, -heappop(self.max_heap))

        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
            
    def findMedian(self) -> float:
        n1, n2 = len(self.max_heap), len(self.min_heap)
        if n1 == 0: return 0
        if n1 == n2:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()