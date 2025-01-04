class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node):
            if node == destination:
                return True
            visited.add(node)


            for next in adj[node]:
                if next not in visited:
                    if (dfs(next)):
                        return True
            
            return False

        return dfs(source)
            