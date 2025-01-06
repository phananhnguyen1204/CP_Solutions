class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        for r in range(1, m):
            for c in range(0, n):
                above = matrix[r - 1][c]
                above_left = matrix[r-1][c-1] if c - 1 >= 0 else float("inf")
                above_right = matrix[r-1][c + 1] if c + 1 < n else float("inf")

                matrix[r][c] = min(above, above_left, above_right) + matrix[r][c]

        min_sum = float("inf")
        for c in range(n):
            min_sum = min(matrix[m-1][c], min_sum)

        return min_sum