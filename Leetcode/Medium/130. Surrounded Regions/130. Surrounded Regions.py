class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            visited.add((r, c))
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O' and (nr, nc) not in visited:
                    dfs(nr, nc)

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r == 0 or c == 0 or r == m -1 or c == n - 1):
                    dfs(r, c) 
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r, c) in visited: continue
                board[r][c] = 'X'
        return board