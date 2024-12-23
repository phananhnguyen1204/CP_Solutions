class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]

        val = 1
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        r = c = 0
        visited = set()

        def valid(r, c):
            return r < n and r >= 0 and c >= 0 and c < n and (r, c) not in visited

        while val <= n ** 2:
            res[r][c] = val
            visited.add((r, c))
            dr, dc = dirs[dir_idx]

            if not valid(r + dr, c + dc):
                dir_idx = (dir_idx + 1) % 4

            dr, dc = dirs[dir_idx]
            r, c = r + dr, c + dc
            val += 1
        
        return res


            