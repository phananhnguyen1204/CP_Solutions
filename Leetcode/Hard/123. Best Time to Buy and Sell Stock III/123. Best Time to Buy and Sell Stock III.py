class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [3,3,5,0,0,3,1,4] -> 6

        dfs(i, is_buy, cnt_transaction) -> 
        if is_buy is True:
         profit = max(dfs(i + 1, is_buy, cnt_transaction), prices[i] + dfs(i + 1, !is_buy, cnt_transaction))
        else:
            profit = max(dfs(i + 1, is_buy, cnt_transaction), -prices[i] + dfs(i + 1, !is_buy, cnt_transaction))
        """
        dp = {}
        def dfs(i, is_buy, cnt):
            if cnt == 2 or i >= len(prices):
                return 0
            if (i, is_buy, cnt) in dp:
                return dp[(i, is_buy, cnt)]
            profit = 0
            if is_buy:
                profit = max(dfs(i + 1, True, cnt), prices[i] + dfs(i + 1, False, cnt + 1))
            else:
                profit = max(dfs(i + 1, False, cnt), -prices[i] + dfs(i + 1, True, cnt))
            dp[(i, is_buy, cnt)] = profit
            return profit
        return dfs(0, False, 0)
                

        