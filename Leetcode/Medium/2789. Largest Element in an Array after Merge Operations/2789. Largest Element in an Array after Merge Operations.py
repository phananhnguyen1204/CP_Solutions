class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        """
        need to find nums[i] <= nums[i + 1]
        traverse from the end
        """

        n = len(nums)
        res = nums[n-1]
        curr = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if nums[i] > curr:
                curr = nums[i]
            else:
                curr += nums[i]
            res = max(res, curr)
        return res