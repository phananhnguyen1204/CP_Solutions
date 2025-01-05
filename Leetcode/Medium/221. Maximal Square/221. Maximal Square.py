class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        1 1 1
        1 2 1 

        """

        m, n = len(matrix), len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        res = 0
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if matrix[r-1][c-1] == '1':
                    dp[r][c] = min(dp[r][c-1], dp[r-1][c-1], dp[r-1][c]) + 1
                res = max(dp[r][c] * dp[r][c], res)

        return res        