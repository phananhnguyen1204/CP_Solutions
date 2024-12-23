class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        steps = 1
        res = []

        def valid(r, c):
            return r < rows and r >= 0 and c >= 0 and c < cols

        while len(res) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    if valid(rStart, cStart):
                        res.append([rStart, cStart])
                    dr, dc = dirs[dir_idx]
                    rStart, cStart = rStart + dr, cStart + dc
                dir_idx = (dir_idx + 1) % 4

            steps += 1

        return res

            
