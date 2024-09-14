class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
#         [4]
#     [1.5]  [1.5]
#  [0.25] [0.5] [0.25] [0.25]

        prev = [poured]
        for row in range(1, query_row + 1):
            curr = [0] * (query_row + 1)
            for i in range(row):
                extra = prev[i] - 1
                if extra > 0:
                    curr[i] += extra / 2
                    curr[i + 1] += extra / 2
            prev = curr
        return min(1, prev[query_glass])