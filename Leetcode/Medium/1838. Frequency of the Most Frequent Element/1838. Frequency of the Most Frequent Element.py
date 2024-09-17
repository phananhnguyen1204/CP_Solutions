class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        res = 0
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while nums[r] * (r - l + 1) > curr_sum + k:
                curr_sum -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res
