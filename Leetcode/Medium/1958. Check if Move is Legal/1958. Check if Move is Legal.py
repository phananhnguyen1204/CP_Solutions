class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]]
        m, n = len(board), len(board[0])

        def check(dir):
            r = rMove + dir[0]
            c = cMove + dir[1]
            curr_len = 2
            while 0 <= r < m and 0 <= c < n:
                if board[r][c] == ".": return False
                if board[r][c] == color: 
                    return curr_len >= 3
                curr_len += 1
                r += dir[0]
                c += dir[1]
            return False

        for dir in directions:
            if check(dir):
                return True
        return False
            