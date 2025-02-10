class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        pair of indices (unique pair since i < j)
        """
        MOD = 10 ** 9 + 7
        freq = defaultdict(int)
        def rev(x):
            return int(str(x)[::-1])

        res = 0
        for num in nums:
            key = num - rev(num)
            if key in freq:
                res += freq[key]
            freq[key] += 1
        return res % MOD