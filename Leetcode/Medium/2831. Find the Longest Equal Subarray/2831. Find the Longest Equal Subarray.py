class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        """
        subarray -> can not sort 
        delete at most -> trying to delete all the non equal element in nums[l:r]
        delete the number that does not have the most freq
        # of delete = len of array - freq of the most freq element in nums[l:r]
        if window invalid -> if we keep expending -> still invalid -> need to shrink window
        -> sliding window
        """

        n = len(nums)

        max_freq = 0
        res = 0
        freq = defaultdict(int)
        l = 0

        for r in range(n):
            freq[nums[r]] += 1
            max_freq = max(max_freq, freq[nums[r]])
            while (r - l + 1) - max_freq > k:
                freq[nums[l]] -= 1
                l += 1 
        return max_freq
         