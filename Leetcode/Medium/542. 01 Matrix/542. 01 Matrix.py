class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = deque()
        visited = set()
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def valid(r, c):
            return r >= 0 and r < m and c >=0 and c < n


        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))

        while q:
            r, c, dist = q.popleft()
            mat[r][c] = dist
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if valid(nr, nc) and (nr, nc) not in visited:
                    q.append((nr, nc, dist + 1))
                    visited.add((nr, nc))


        return mat