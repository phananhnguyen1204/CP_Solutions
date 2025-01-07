class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        k = len(costs[0])
        n = len(costs)
        memo = {}
        
        def dfs(i, color):
            if i == 0:
                return costs[i][color]
            
            if (i, color) in memo:
                return memo[(i, color)]

            total_cost = float("inf")

            for j in range(k):
                if j == color:
                    continue
                total_cost = min(total_cost, dfs(i - 1, j))
            
            memo[(i, color)] = total_cost + costs[i][color]
            return memo[(i, color)]

        res = float("inf")

        for i in range(k):
            res = min(res, dfs(n - 1, i))

        return res