class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited1 , visited2 = set(), set()
        m, n = len(grid1), len(grid1[0])
        cnt = 0
        visited = set()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            visited.add((r, c))
            if grid1[r][c] != 1:
                nonlocal flag
                flag = False
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid2[nr][nc] == 1:
                    dfs(nr, nc)

        for r in range(m):
            for c in range(n):
                if grid2[r][c] == 1 and (r, c) not in visited:
                    flag = True
                    dfs(r, c)
                    if flag: cnt += 1
        return cnt
        