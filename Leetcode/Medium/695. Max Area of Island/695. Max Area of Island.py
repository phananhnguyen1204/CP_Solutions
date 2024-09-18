class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        area = 0

        def dfs(r, c, area):
            visited.add((r, c))

            for dir in directions:
                nr = r + dir[0]
                nc = c + dir[1]
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 1:
                    dfs(nr, nc, area + 1)
            

        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == 1:
                    area = 0
                    dfs(r, c, area)
                    res = max(res, area)
        return res