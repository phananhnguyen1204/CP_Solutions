class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        seen = set()
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0: return 0
            fish = grid[r][c]
            grid[r][c] = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                fish += dfs(nr, nc)
            return fish

        for r in range(m):
            for c in range(n):
                # water cell
                if grid[r][c] != 0 and (r, c) not in seen:
                    res = max(res, dfs(r, c))

        return res