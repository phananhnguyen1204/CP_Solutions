class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        res = 0
        
        def dfs(r, c):
            visited.add((r, c))
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 1:
                    dfs(nr, nc)
        
        def bfs():
            nonlocal res
            q = deque(visited)
            print(q)
            while q:
                size = len(q)
                for i in range(size):
                    (r, c) = q.popleft()
                    for dir in directions:
                        nr, nc = r + dir[0], c + dir[1]                        
                        if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                            if grid[nr][nc] == 1: return res
                            q.append((nr, nc))
                            visited.add((nr, nc))
                res += 1


        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()