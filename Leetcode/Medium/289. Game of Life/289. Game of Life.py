class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]]
        """
        care aboue:
        cell live but previously died
        cell died but previously live
        """
        for i in range(m):
            for j in range(n):
                cnt = 0
                for dir in dirs:
                    r = i + dir[0]
                    c = j + dir[1]
                    if r >=0 and r < m and c >= 0 and c < n:
                        if abs(board[r][c]) == 1:
                            cnt += 1

                if board[i][j] == 1 and (cnt < 2 or cnt > 3):
                    board[i][j] = -1
                if board[i][j] == 0 and cnt == 3:
                    board[i][j] = 2
                


        for r in range(m):
            for c in range(n):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
                        