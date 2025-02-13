from heapq import heappush, heappop
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        max_heap = []
        target = curr_sum = sum(nums)
        for num in nums:
            heappush(max_heap, -num)
        res = 0
        while curr_sum > (target / 2):
            num = heappop(max_heap)
            curr_sum += num / 2
            heappush(max_heap, num / 2)
            res += 1
        return res
            