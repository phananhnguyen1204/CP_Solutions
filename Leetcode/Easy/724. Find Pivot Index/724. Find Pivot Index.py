class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)    
        prefix_sum = [0] * n

        for i, num in enumerate(nums):
            prefix_sum[i] = num if i == 0 else num + prefix_sum[i-1]
        
        for i in range(n):
            left_sum = 0 if i == 0 else prefix_sum[i-1]
            right_sum = prefix_sum[n-1] - prefix_sum[i]

            if left_sum == right_sum:
                return i
        
        return -1