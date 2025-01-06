class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        n = len(prices) 

        def dfs(i, state):
            if (i, state) in memo:
                return memo[(i, state)]
            if i >= len(prices):
                return 0
            profit = 0
            if state:
                profit = max(-prices[i] + dfs(i + 1, False), dfs(i + 1, True))
            else:
                profit = max(prices[i] + dfs(i + 2, True), dfs(i + 1, False))

            memo[(i, state)] = profit
            return memo[(i, state)]

        return dfs(0, True)