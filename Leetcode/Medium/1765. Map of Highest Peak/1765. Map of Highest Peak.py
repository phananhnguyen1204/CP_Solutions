class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        visited = set()

        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1: 
                    q.append((r, c, 0))
                    visited.add((r, c))

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        while q:
            r, c, height = q.popleft()
            isWater[r][c] = height
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if valid(nr, nc) and (nr, nc) not in visited:
                    q.append((nr, nc, height + 1))
                    visited.add((nr, nc))

        return isWater

            
    