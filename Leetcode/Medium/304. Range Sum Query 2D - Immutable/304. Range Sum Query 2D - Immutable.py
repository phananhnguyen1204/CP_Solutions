class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                left = self.prefix[r][c-1] if c > 0 else 0
                up = self.prefix[r-1][c] if r > 0 else 0
                mid = self.prefix[r-1][c-1] if r > 0 and c > 0 else 0
                self.prefix[r][c] = matrix[r][c] + left + up - mid
                    
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        up = self.prefix[row1-1][col2] if row1 > 0 else 0
        mid = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.prefix[row2][col2] - left - up + mid


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)