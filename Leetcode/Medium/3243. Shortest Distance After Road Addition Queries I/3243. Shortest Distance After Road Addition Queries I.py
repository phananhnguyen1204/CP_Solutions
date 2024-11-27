class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        adj = [[] for _ in range(n)]
        for i in range(n-1):
            adj[i].append(i+1)

        def bfs():
            q = deque()
            visited = set()
            q.append((0, 0))
            visited.add(0)

            while q:
                curr, dist = q.popleft()
                if curr == n - 1:
                    return dist
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, dist + 1))
            
            return -1
        
        for u, v in queries:
            adj[u].append(v)
            res.append(bfs())
        return res