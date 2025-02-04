class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        res = nums[0]
        curr_sum = nums[0]

        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                curr_sum = 0
            curr_sum += nums[i]
            res = max(res, curr_sum)
        return res