class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        
        row_map = [set() for _ in range(rows)]
        col_map = [set() for _ in range(cols)]
        box_map = [set() for _ in range(9)]


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '.': 
                    continue
                idx = (r // 3) * 3 + (c // 3)
                
                if board[r][c] in row_map[r] or board[r][c] in col_map[c] or board[r][c] in box_map[idx]:
                    return False
                
                row_map[r].add(board[r][c])
                col_map[c].add(board[r][c])
                box_map[idx].add(board[r][c])
            
        return True
                
