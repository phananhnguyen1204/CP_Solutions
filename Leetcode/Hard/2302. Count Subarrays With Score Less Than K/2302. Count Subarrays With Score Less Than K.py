class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        l = 0
        total = 0

        for r in range(n):
            total += nums[r]
            while total * (r - l + 1) >= k:
                total -= nums[l]
                l += 1
            res += r - l + 1
        return res
                