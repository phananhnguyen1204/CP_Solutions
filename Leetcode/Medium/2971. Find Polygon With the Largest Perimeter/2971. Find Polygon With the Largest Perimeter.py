class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prev_total = 0
        res = -1 
        for i, num in enumerate(nums):
            if i >= 2 and num < prev_total:
                res = prev_total + num
            prev_total += num
        return res