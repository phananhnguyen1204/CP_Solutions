class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        q = deque()
        visisted = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    visisted.add((r, c))
                    q.append((r, c))
        while q:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                for dir in directions:
                    nr = r + dir[0]
                    nc = c + dir[1]
                    if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == 2147483647 and (nr, nc) not in visisted:
                        visisted.add((nr, nc))
                        q.append((nr, nc))
                        rooms[nr][nc] = rooms[r][c] + 1

                


        
        