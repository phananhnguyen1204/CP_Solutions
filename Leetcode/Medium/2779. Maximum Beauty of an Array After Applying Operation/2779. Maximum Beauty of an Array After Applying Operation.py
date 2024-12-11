class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()
        l = 0
        for r in range(len(nums)):
            while l <= r and nums[r] - nums[l] > 2 * k:
                l += 1
            res = max(res, r - l + 1)
        
        return res