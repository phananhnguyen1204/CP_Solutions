class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        for r in range(m):
            for c in range(n):
                heappush(diagonals[r - c], mat[r][c])
        
        for r in range(m):
            for c in range(n):
                mat[r][c] = heappop(diagonals[r - c])

        return mat