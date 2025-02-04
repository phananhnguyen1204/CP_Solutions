class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        if n == 1: return 1

        start = 0
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                len_subarray = i - start
                res += (len_subarray * (len_subarray + 1)) // 2
                start = i
        res += ((n - start) * (n - start + 1)) // 2
        return res