class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        def tranpose(matrix):
            for r in range(m):
                for c in range(r + 1, n):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        def reflex(matrix):
            for r in range(m):
                for c in range(n // 2):
                    matrix[r][c], matrix[r][-1-c] = matrix[r][-1-c], matrix[r][c]
        
        tranpose(matrix)
        reflex(matrix)
        return matrix