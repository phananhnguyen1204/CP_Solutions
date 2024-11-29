from heapq import heappush, heappop
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        m, n = len(grid), len(grid[0])
        visited = set()

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n and (r, c) not in visited

        pq = [(0, 0, 0)] #[(time, r, c)]

        while pq:
            time, r, c = heappop(pq)
            if r == m-1 and c == n-1:
                return time

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if not valid(nr, nc): continue
                wait_time = 1 if (grid[nr][nc] - time) % 2 == 0 else 0
                next_time = max(time + 1, grid[nr][nc] + wait_time)
                visited.add((nr, nc))
                heappush(pq, (next_time, nr, nc))

        return -1