class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        visited = set()
        def bfs(s, d):
            if s not in adj or d not in adj: return -1
            q = deque()
            # visisted = set()
            q.append((s, 1))
            visited.add(s)
            while q:
                curr, dis = q.popleft()
                if curr == d: return dis
                for nextNode, w in adj[curr]:
                    if nextNode not in visited:
                        visited.add(nextNode)
                        q.append((nextNode, w * dis))
            return -1
        
        res = []
        for s, d in queries:
            visited = set()
            res.append(bfs(s, d))
        return res
                        


        