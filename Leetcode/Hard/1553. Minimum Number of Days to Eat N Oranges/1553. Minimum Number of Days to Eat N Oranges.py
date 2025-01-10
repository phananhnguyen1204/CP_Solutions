class Solution:
    def minDays(self, n: int) -> int:
        memo = {}
        def dfs(orange):
            if orange <= 2:
                return orange
            if orange in memo:
                return memo[orange]

            min_day = 1 + orange % 2 + dfs(orange // 2)
            min_day = min(min_day, 1 + orange % 3 + dfs(orange // 3))
            memo[orange] = min_day 
            return min_day
        return dfs(n)
            