class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for a, b in edges:
            adj[a].append(b)
            indegree[b] += 1
        
        for i, degree in enumerate(indegree):
            if degree == 0:
                res.append(i)
        return res

        