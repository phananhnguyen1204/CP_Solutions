class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        grid = [[0] * n for _ in range(m)]
        
        for r, c in  walls + guards:
            grid[r][c] = 2

        for x, y in guards:
            for dr, dc in dirs:
                r, c = x, y
                while True:
                    r += dr
                    c += dc
                    if r < 0 or r >= m or c < 0 or c >= n:
                        break
                    if grid[r][c] == 2: 
                        break
                    grid[r][c] = 1
        cnt = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0: cnt += 1
        return cnt