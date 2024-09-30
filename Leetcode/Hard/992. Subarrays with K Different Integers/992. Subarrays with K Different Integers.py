class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            cnt = {}
            l, res = 0, 0
            for r in range(len(nums)):
                cnt[nums[r]] = cnt.get(nums[r], 0) + 1
                while l <= r and len(cnt) >= k:
                    res += len(nums) - r
                    cnt[nums[l]] -= 1
                    if cnt[nums[l]] == 0:
                        del cnt[nums[l]]
                    l += 1
            return res
        return helper(nums, k) - helper(nums, k + 1)