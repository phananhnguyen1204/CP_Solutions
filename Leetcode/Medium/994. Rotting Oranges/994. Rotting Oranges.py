class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        res = 0
        cnt = 0
        directions = [[1, 0], [-1, 0],[0, 1], [0, -1]]
        visited = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    cnt += 1
        if cnt == 0: return 0

        while q:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                for dir in directions:
                    nr, nc = r + dir[0], c + dir[1]
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 1:
                        cnt -= 1
                        visited.add((nr, nc))
                        q.append((nr, nc))
            res += 1
        
        return res - 1 if cnt == 0 else -1
                    
                