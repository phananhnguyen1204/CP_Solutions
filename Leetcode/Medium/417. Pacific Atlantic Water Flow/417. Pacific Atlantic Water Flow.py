class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(heights), len(heights[0])
        pacific_q = deque()
        atlantic_q = deque()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        

        for i in range(m):
            pacific_q.append((i, 0))
            atlantic_q.append((i, n - 1))
        for i in range(n):
            pacific_q.append((0, i))
            atlantic_q.append((m - 1, i))

        def bfs(q):
            visited = set()
            while q:
                r, c = q.popleft()
                visited.add((r, c))
                for dir in directions:
                    nr, nc = r + dir[0], c + dir[1]
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        q.append((nr, nc))
            return visited
        
        pacific = bfs(pacific_q)
        atlantic = bfs(atlantic_q)
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
                