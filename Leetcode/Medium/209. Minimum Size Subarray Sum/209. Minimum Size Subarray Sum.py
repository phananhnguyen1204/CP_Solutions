class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur_sum = 0
        n = len(nums)
        res = n + 1

        for r in range(len(nums)):
            cur_sum += nums[r]

            while cur_sum >= target:
                res = min(res, r - l + 1)
                cur_sum -= nums[l]
                l += 1
            
        return 0 if res == n + 1 else res