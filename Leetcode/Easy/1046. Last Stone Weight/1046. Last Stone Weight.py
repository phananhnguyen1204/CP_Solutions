from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = []
        for stone in stones:
            heappush(weights, -stone)
        while len(weights) > 1:
            x = heappop(weights) * (-1)
            y = heappop(weights) * (-1)
            if x != y:
                heappush(weights, (-1) * abs(x - y))
        return (-1) * weights[0] if weights else 0