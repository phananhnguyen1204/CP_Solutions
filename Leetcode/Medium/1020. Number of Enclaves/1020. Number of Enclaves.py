class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        visited = set()
        flag = False
        area = 0
        res = 0
        def isBorder(r, c):
            return r == 0 or c == 0 or r == m - 1 or c == n - 1
        def dfs(r, c):
            nonlocal area
            area += 1
            visited.add((r, c))
            if isBorder(r, c):
                nonlocal flag
                flag = True
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 1:
                    dfs(nr, nc)


        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == 1:
                    flag = False
                    area = 0
                    dfs(r, c)
                    if not flag: 
                        print(area)
                        res += area

        return res