class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        # row, col -> row-1, col + 1
        # row, col -> row + 1, col -1

        index = 0
        res = [0] * (m * n)
        r, c = 0, 0

        while index < m * n:
            # Move up
            while r >= 0 and c < n:
                res[index] = mat[r][c]
                index += 1
                r -= 1
                c += 1
            
            r += 1
            if c >= n:
                c -= 1
                r += 1
            
            #Move down
            while r < m and c >= 0:
                res[index] = mat[r][c]
                index += 1
                r += 1
                c -= 1
            
            c += 1
            if r >= m:
                c += 1
                r -= 1
        
        return res
            