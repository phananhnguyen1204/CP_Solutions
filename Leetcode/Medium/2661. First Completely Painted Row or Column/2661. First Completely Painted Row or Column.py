class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Optimize lookup -> using hashmap
        # Optimize checking wheter a row or column will be completely painted
        val_idx_map = {}
        
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                val_idx_map[mat[r][c]] = [r, c]

        rows = defaultdict(set)
        cols = defaultdict(set)

        for i in range(len(arr)):
            val = arr[i]
            r, c = val_idx_map[val]
            rows[r].add(val)
            cols[c].add(val)
            if len(rows[r]) == n:
                return i
            if len(cols[c]) == m:
                return i

        return -1 