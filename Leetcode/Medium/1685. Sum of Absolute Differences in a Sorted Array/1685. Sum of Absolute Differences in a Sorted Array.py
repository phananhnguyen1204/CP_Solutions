class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = []
        n = len(nums)
        for i, num in enumerate(nums):
            prefix.append(num)
        res = [0] * n
        for i in range(n):
            prefix[i] = prefix[i-1] + prefix[i] if i > 0 else prefix[i]
        for i in range(n):
            left = nums[i] * i - (prefix[i - 1] if i > 0 else 0)
            right_len = n - 1 - i
            right = prefix[n - 1] - prefix[i] - right_len * nums[i]
            res[i] = left + right

        return res
        