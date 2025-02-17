class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        n = len(nums)
        nums.sort()
        res = 0

        def backtrack(start):
            nonlocal res
            res += 1
            for i in range(start, n):
                if freq[nums[i] - k] == 0:
                    freq[nums[i]] += 1
                    backtrack(i + 1)
                    freq[nums[i]] -= 1
        backtrack(0)
        return res - 1

         