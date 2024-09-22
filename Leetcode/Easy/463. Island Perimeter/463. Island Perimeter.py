class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0: 
                return 1
            if (r, c) in visited: return 0
            visited.add((r, c))
            per = 0
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                per += dfs(nr, nc)
            return per
            



        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res += dfs(r, c)
                    return res
        return -1
