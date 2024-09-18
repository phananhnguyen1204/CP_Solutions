class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            visited.add((r, c))

            for dir in directions:
                nr = r + dir[0]
                nc = c + dir[1]
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1" and (nr, nc) not in visited:
                    dfs(nr, nc)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    dfs(r, c)
        return res
            