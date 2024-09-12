class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        left, right = 0, sum(grid[0])
        n = len(grid[0])
        res = float("inf")
        for c in range(n):
            right -= grid[0][c]
            res = min(res, max(right, left))
            left += grid[1][c]
        return res

