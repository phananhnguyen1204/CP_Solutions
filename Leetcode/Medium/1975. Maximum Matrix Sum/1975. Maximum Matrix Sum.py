class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix) 
        res = 0
        cnt = 0
        min_val = float("inf")
        for r in range(n):
            for c in range(n):
                res += abs(matrix[r][c])
                if matrix[r][c] < 0:
                    cnt += 1
                min_val = min(min_val, abs(matrix[r][c]))
        
        if cnt % 2 == 1:
            res -= 2 * min_val
        
        return res
                