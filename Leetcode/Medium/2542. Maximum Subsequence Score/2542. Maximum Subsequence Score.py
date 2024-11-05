from heapq import heappush, heappop
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key = lambda p: p[1], reverse=True)
        
        min_heap = []
        res = 0
        total = 0
        for n1, n2 in pairs:
            total += n1
            heappush(min_heap, n1)
            if len(min_heap) > k:
                total -= heappop(min_heap)
            if len(min_heap) == k:
                res = max(total * n2, res)
        
        return res

            