class Solution:
    def numWays(self, n: int, k: int) -> int:
        # ways(ith) = (k-1) ways(i-1)
        # ways(i) = 1* way(i - 2)
        
        memo = {}

        def dfs(i):
            if i <= 0:
                return 0
            
            if i == 1:
                return k

            if i == 2:
                return k * k

            if i in memo:
                return memo[i]

            memo[i] = (k-1) * (dfs(i - 1) + dfs(i - 2))
            return memo[i]


        return dfs(n)
                