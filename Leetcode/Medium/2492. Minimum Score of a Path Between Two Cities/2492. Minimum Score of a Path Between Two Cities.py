class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        visited = set()
        for a, b, dis in roads:
            adj[a].append((b, dis))
            adj[b].append((a, dis))

        res = float("inf")
        def dfs(u):
            nonlocal res
            visited.add(u)
            for v, dis in adj[u]:
                res = min(res, dis)
                if v not in visited:
                    dfs(v)

        dfs(1)
        return res