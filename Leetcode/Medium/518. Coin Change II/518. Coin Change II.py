class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, amount):
            if amount == 0:
                return 1
            if amount < 0 or i >= len(coins):
                return 0

            if (i, amount) in memo:
                return memo[(i, amount)]

            pick = dfs(i, amount - coins[i])
            skip = dfs(i + 1, amount)

            memo[(i, amount)] = pick + skip
            return memo[(i, amount)]

        return dfs(0, amount)