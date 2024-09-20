class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for connection in connections:
            a, b = connection
            adj[b].append((a, 0))
            adj[a].append((b, 1))
        
        res = 0
        visited = set()
        def dfs(node):
            nonlocal res
            visited.add(node)
            
            for next_node, cost in adj[node]:
                if next_node not in visited:
                    res += cost
                    dfs(next_node)
        dfs(0)
        return res