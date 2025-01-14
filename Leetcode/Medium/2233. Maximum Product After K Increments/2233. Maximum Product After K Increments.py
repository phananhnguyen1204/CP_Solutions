from heapq import heappush, heappop
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        min_heap = []
        for num in nums: heappush(min_heap, num)
        res = 1
        while k:
            val = heappop(min_heap)
            heappush(min_heap, val + 1)
            k -= 1

        while min_heap:
            res *= heappop(min_heap) % MOD

        return res % MOD