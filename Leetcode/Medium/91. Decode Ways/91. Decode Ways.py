class Solution:
    def numDecodings(self, s: str) -> int:
        
        """
        dfs(i)

        "f(2326) -> f(326) + f(26)

        f(326) -> f(26) + f() 

        dfs(i):  # way to decode
        """ 
        memo = {}
        if s == "0":
            return 0

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]

            total_ways = dfs(i + 1)
            if i < len(s) - 1 and int(s[i: i + 2]) <= 26:
                total_ways += dfs(i + 2)
            
            memo[i] = total_ways
            return memo[i]

        return dfs(0)