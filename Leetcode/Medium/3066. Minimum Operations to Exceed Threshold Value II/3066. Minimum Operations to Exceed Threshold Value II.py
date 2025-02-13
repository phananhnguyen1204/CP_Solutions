from heapq import heappush, heappop
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = []
        res = 0
        for num in nums:
            heappush(min_heap, num)
        
        while len(min_heap) >= 2 and min_heap[0] < k:
            x = heappop(min_heap)
            y = heappop(min_heap)
            heappush(min_heap, x * 2 + y)
            res += 1
        return res