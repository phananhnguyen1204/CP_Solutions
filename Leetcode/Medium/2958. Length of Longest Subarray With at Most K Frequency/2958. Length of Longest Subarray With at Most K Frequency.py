class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = {}
        l, res = 0, 0
        for r in range(len(nums)):
            cnt[nums[r]] = cnt.get(nums[r], 0) + 1
            while cnt[nums[r]] > k:
                cnt[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res