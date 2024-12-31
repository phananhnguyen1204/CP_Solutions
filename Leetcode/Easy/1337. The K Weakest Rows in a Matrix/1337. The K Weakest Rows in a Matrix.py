from heapq import heappush, heappop
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        min_heap = []

        for r in range(m):
            cnt = 0
            for c in range(n):
                if mat[r][c] == 1:
                    cnt += 1

            heappush(min_heap, (cnt, r))

        res = []

        for i in range(k):
            res.append(heappop(min_heap)[1])

        return res