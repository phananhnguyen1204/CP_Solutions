class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def min_cost(i):
            if i <= 1:
                return 0

            if i in memo:
                return memo[i]
            
            memo[i] = min(cost[i - 1] + min_cost(i - 1), cost[i - 2] + min_cost(i - 2))

            return memo[i]
        return min_cost(len(cost)) 