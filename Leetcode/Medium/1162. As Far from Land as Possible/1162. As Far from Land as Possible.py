class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: 
                    q.append([r, c])
                    visited.add((r, c))
        level = 0
        res = float("-inf")
        while q:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                for dir in directions:
                    nr, nc = r + dir[0], c + dir[1]
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append([nr, nc])
                        res = max(res, level + 1)
            level += 1
        return -1 if res == float("-inf") else res