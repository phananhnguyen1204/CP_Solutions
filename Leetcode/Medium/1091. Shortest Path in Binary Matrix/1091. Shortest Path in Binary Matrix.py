class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        visited = set()
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n - 1] == 1: return -1
        
        q = deque()
        q.append((0, 0))
        grid[0][0] = 1
        while q:
            r, c = q.popleft()
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
        
        return grid[m - 1][n - 1] if grid[m - 1][n - 1] != 0 else -1