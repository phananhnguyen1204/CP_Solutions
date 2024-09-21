class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        res = []

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
        
        def union(u, v):
            nonlocal res
            pu = find(u)
            pv = find(v)
            if pu == pv:
                res.append(u)
                res.append(v)
            if rank[pu] > rank[pv]:
                parent[pv] = pu
                rank[u] += 1
            elif rank[pu] < rank[pv]:
                parent[pu] = pv
                rank[pv] += 1
            else:
                parent[pv] = pu
                rank[pu] += 1
         
        for a, b in edges:
            union(a, b)
        return res