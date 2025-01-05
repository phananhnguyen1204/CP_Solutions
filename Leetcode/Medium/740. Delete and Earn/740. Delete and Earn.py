class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memo = {}
        max_element = max(nums)
        min_element = min(nums)

        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += num

        def dfs(i):
            if i < min_element:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(freqs[i] + dfs(i - 2), dfs(i - 1))
            return memo[i]

        return dfs(max_element)