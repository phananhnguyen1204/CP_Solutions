class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_idx = {0 : -1}
        res = 0
        total = 0
        for i, num in enumerate(nums):
            total += num
            remain = total - k
            if remain in sum_idx:
                res = max(res, i - sum_idx[remain])
            if total not in sum_idx:
                sum_idx[total] = i

        return res   
            