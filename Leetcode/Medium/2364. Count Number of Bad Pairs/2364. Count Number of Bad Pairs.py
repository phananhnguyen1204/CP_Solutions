class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        nums[i] - i != nums[j] - j
        find pairs that nums[i] - i == nums[j] - j
        # bad pairs = total pairs - good pairs
        """

        cnt = defaultdict(int) # map target -> # of target
        n = len(nums)

        good_pairs = 0
        for i in range(n):
            target = nums[i] - i
            good_pairs += cnt[target]
            cnt[target] += 1
        
        return n * (n - 1) // 2 - good_pairs

