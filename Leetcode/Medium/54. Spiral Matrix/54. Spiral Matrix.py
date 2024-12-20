class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        
        # right -> down -> left -> up

        res = []

        startRow = startCol = 0
        endRow = rows - 1
        endCol = cols - 1
        
        while len(res) < rows * cols:
            # Move right
            for c in range(startCol, endCol + 1):
                res.append(matrix[startRow][c])

            startRow += 1
            # Move down
            
            for r in range(startRow, endRow + 1):
                res.append(matrix[r][endCol])

            endCol -= 1
            if startRow <= endRow:
                # Move left
                for c in range(endCol, startCol - 1, -1):
                    res.append(matrix[endRow][c])
                
            endRow -= 1
            if startCol <= endCol:
                # Move up
                for r in range(endRow, startRow - 1, -1):
                    res.append(matrix[r][startCol])

            startCol += 1
    
        return res

        