from heapq import heappush, heappop
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1: return 0

        min_heap = []
        for stick in sticks:
            heappush(min_heap, stick)

        costs = 0
        while len(min_heap) > 1:
            x = heappop(min_heap)
            y = heappop(min_heap)
            costs += x + y
            heappush(min_heap, x + y)
        
        return costs
