class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0) , (-1, 0), (0, 1), (0, -1)]
        q = deque()
        visited = set()
        
        q.append((0, 0, 0))
        
        while q:
            r, c, cnt = q.popleft()
            if r == m - 1 and c == n - 1:
                return cnt

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in visited: continue

                if grid[nr][nc] == 0:
                    q.appendleft((nr, nc, cnt))
                else:
                    q.append((nr, nc, cnt + 1))
                visited.add((nr, nc))

        return -1