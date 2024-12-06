from heapq import heappush, heappop
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        stones = []
        for pile in piles:
            heappush(stones, -pile)
        
        for i in range(k):
            remove = -heappop(stones)
            heappush(stones, -(remove - remove // 2))
        
        return -sum(stones)
            