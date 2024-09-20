class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        res.sort()
        return res