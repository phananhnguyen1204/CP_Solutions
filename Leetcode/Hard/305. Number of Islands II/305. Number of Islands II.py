class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """
        turn 2D -> 1D: every call has index = r * n + c
        parent: -1: no land
                otherwise: parent of ith
        query can have duplicate (same cell turns into 1)

        [
            1 1 
            0 1
        ]
        res = [1]
        """

        parent = defaultdict(int)
        rank = defaultdict(int)
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        for r in range(m):
            for c in range(n):
                parent[r * n + c] = -1

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            nonlocal islands
            pu, pv = find(u), find(v)
            # same island
            if pu == pv: return
            if rank[pu] > rank[pv]:
                parent[pv] = pu
            elif rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                parent[pv] = pu
                rank[pu] += 1
            islands -= 1
        
        res = []
        for r, c in positions:
            i = r * n + c
            # already process this land
            if parent[i] == -1:
                islands += 1
                parent[i] = i
            # found_new_island = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if valid(nr, nc):
                    ni = nr * n + nc
                    # neighbor is land
                    if parent[ni] != -1:
                        union(i, ni)
            # if found_new_island: islands += 1
            # else: islands -= 1
            res.append(islands)
        return res

        