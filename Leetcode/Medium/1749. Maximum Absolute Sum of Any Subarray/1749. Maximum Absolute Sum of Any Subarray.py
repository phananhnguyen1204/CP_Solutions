class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        1st approach
        abs(sum) = min sum or max sum
        abs(sum) >=  max sum = (max_prefix - min_prefix)

        run kadance twice
        """
        max_sum = 0
        total = 0
        n = len(nums)
        for i in range(n):
            total += nums[i]
            max_sum = max(total, max_sum)
            total = max(0, total)
        
        min_sum = 0
        total = 0
        for i in range(n):
            total += nums[i]
            min_sum = min(min_sum, total)
            total = min(0, total)
        return max(abs(min_sum), abs(max_sum))
        