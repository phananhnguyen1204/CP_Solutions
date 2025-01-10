class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_cost = 0

        def valid(r, c):
            return r >= 0 and r < m and c >=0 and c < n
        
        def dfs(r, c):
            temp = grid[r][c] 
            grid[r][c] = 0 
            total_cost = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if valid(nr, nc) and grid[nr][nc] != 0:
                    total_cost = max(dfs(nr, nc), total_cost)
            grid[r][c] = temp
            return total_cost + grid[r][c]

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    max_cost = max(max_cost, dfs(r, c))
        return max_cost

