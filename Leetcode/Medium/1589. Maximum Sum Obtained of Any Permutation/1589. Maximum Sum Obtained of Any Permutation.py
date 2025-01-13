class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0] * n
        MOD = 10 ** 9 + 7

        for s, e in requests:
            prefix[s] += 1
            if e + 1 < n:
                prefix[e + 1] -= 1

        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        prefix = sorted(prefix)
        nums = sorted(nums)

        res = 0
        for i in range(n):
            res += prefix[i] * nums[i]

        return res % MOD