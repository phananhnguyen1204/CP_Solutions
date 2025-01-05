class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # index, is_buy, k
        memo = {}

        def dfs(i, is_buy, k):
            if i >= len(prices) or k == 0:
                return 0

            if (i, is_buy, k) in memo:
                return memo[(i, is_buy, k)]

            profit = 0
            if is_buy:
                profit = max(-prices[i] + dfs(i + 1, False, k), dfs(i + 1, True, k))
            else:
                profit = max(prices[i] + dfs(i + 1, True, k - 1), dfs(i + 1, False, k))

            memo[(i, is_buy, k)] = profit

            return profit

        return dfs(0, True, k)

