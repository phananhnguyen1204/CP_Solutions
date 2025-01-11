class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        
        if x > total:
            return -1

        target = total - x
        start = 0
        max_len = -1

        curr_sum = 0
        for end in range(n):
            curr_sum += nums[end]
            while curr_sum > target and start <= end:
                curr_sum -= nums[start]
                start += 1
            
            if curr_sum == target:
                max_len = max(max_len, end - start + 1)

        return n - max_len if max_len != -1 else -1
