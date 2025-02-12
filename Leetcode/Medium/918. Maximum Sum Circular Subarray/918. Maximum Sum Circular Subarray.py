class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        2 types: - sum that that circular (simple Kadane)
                - sum that circular (total - min_sum)
        """
        min_sum, max_sum = float("inf"), float("-inf")
        total1 = total2 = 0

        for i in range(len(nums)):
            total1 += nums[i]
            total2 += nums[i]
            min_sum = min(min_sum, total2)
            max_sum = max(max_sum, total1)
            total1 = max(0, total1)
            total2 = min(0, total2)
        if min_sum == sum(nums): return max_sum
        return max(sum(nums) - min_sum, max_sum)