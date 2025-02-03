class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1
        
        res = 0
        cnt = 1
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                cnt = 1
            else:
                cnt += 1
            res = max(res, cnt)

        cnt = 1
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                cnt = 1
            else:
                cnt += 1
            res = max(res, cnt)

        return res

