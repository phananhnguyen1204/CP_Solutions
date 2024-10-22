class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        freqs = [0] * (max(nums) + n)
        res = 0

        for num in nums:
            freqs[num] += 1

        for i in range(len(freqs) - 1):
            if freqs[i] <= 1: continue
            duplicates = freqs[i]
            res += duplicates - 1
            freqs[i + 1] += duplicates - 1
            freqs[i] = 1
        
        return res
