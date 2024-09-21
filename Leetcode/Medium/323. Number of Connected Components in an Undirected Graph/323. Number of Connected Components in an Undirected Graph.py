class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            visited.add(node)
            for next_node in adj[node]:
                if next_node not in visited:
                    dfs(next_node)
        
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res
    

