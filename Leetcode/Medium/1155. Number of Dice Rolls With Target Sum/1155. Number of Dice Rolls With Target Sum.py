class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        memo = {}

        def dfs(i, target):
            if target < 0:
                return 0

            if i == 0:
                return 1 if 0 == target else 0

            if (i, target) in memo:
                return memo[(i, target)]

            ways = 0
            for val in range(1, k + 1):
                ways = (ways + dfs(i - 1, target - val)) % MOD
            memo[(i, target)] = ways
            return memo[(i, target)]
        
        return dfs(n, target)