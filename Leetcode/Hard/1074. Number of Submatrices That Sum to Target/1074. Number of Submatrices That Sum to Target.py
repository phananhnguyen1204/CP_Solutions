class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])

        cnt = defaultdict(int)
        res = 0
        prefix = [[0] * n for _ in range(m)]
        cnt[0] = 1
        for r in range(m):
            for c in range(n):
                val1 = prefix[r - 1][c] if r > 0 else 0
                val2 = prefix[r - 1][c - 1] if (r > 0 and c > 0) else 0
                val3 = prefix[r][c - 1] if c > 0 else 0
                prefix[r][c] = matrix[r][c] + val1 - val2 + val3

        for r1 in range(m):
            for r2 in range(r1, m):
                cnt = defaultdict(int)
                cnt[0] = 1
                for c in range(n):
                    val2 = prefix[r2][c]
                    val1 = prefix[r1 - 1][c] if r1 > 0 else 0
                    submatrix_sum = val2 - val1
                    res += cnt[submatrix_sum - target]
                    cnt[submatrix_sum] += 1
        return res