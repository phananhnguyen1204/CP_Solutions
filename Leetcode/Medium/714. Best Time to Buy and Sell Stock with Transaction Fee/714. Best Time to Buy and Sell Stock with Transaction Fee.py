class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}

        def dfs(i, is_buy):
            if i >= len(prices):
                return 0

            if (i, is_buy) in memo:
                return memo[(i, is_buy)]

            profit = 0
            if is_buy:
                profit = max(-prices[i] + dfs(i + 1, False), dfs(i + 1, True))
            else:
                profit = max(prices[i] + dfs(i + 1, True) - fee, dfs(i + 1, False))

            memo[(i, is_buy)] = profit
            return profit

        return dfs(0, True)