class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [(-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, -2), (-2, -1)]

        visited = set()
        q = deque()
        visited.add((0, 0))
        q.append((0, 0, 0))
        while q:
            r, c, step = q.popleft()
            if r == x and c == y:
                return step
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (nr, nc) in visited:
                    continue
                
                visited.add((nr, nc))
                q.append((nr, nc, step + 1))
        
        return -1
