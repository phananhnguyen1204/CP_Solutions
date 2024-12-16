from heapq import heappush, heappop
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_val = []

        for i, num in enumerate(nums):
            heappush(min_val, (num, i))
        
        for i in range(k):
            curr_min, i = heappop(min_val)

            curr_min *= multiplier
            heappush(min_val, (curr_min, i))
            nums[i] = curr_min

        return nums
            