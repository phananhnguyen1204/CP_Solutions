class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        
        visited = [None] * n

        for a, b in edges:
            adj[a].append(b)

        if len(adj[destination]) > 0:
            return False

        def dfs(node): 
            if visited[node] != None:
                return visited[node]
            
            if len(adj[node]) == 0:
                return node == destination

            visited[node] = False
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False

            visited[node] = True
            return True
        
        return dfs(source)

