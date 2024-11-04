from heapq import heappush, heappop
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_elements = []
        curr_min = float("inf")
        for num in nums:
            if num % 2 == 0:
                curr_min = min(curr_min, num)
                heappush(max_elements, -num)
            else:
                curr_min = min(curr_min, num * 2)
                heappush(max_elements, -num * 2)
        
        res = float("inf")
        while max_elements:
            curr_max = -heappop(max_elements)
            res = min(res, curr_max - curr_min)
            if curr_max % 2 == 1:
                break
            heappush(max_elements, -(curr_max // 2))
            curr_min = min(curr_min, curr_max // 2)
        return res

