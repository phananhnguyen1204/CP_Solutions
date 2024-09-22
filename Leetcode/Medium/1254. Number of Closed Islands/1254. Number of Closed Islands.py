class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        res = 0
        check  = False
        def isBorder(r, c):
            return r == m -1 or r == 0 or c == 0 or c == n - 1

        def dfs(r, c):
            nonlocal check
            if isBorder(r, c): check = True
            visited.add((r, c))
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 0:
                    dfs(nr, nc)

        

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and (r, c) not in visited:
                    check = False
                    dfs(r, c)
                    if not check: res += 1
        return res
        