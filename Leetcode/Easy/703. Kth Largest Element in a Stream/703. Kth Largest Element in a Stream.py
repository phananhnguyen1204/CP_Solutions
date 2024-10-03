from heapq import heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        for num in nums:
            heappush(self.minHeap, num)
            if len(self.minHeap) > k:
                heappop(self.minHeap)

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)