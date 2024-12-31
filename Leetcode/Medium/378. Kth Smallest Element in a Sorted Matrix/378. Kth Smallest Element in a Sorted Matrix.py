from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []

        m, n = len(matrix), len(matrix[0])

        for r in range(min(k, m)):
            heappush(min_heap, (matrix[r][0], r, 0))

        for i in range(k):
            element, row_idx, idx = heappop(min_heap)

            if i == k - 1:
                return element

            if idx < m - 1:
                heappush(min_heap, (matrix[row_idx][idx + 1], row_idx, idx + 1))
        
        return -1
