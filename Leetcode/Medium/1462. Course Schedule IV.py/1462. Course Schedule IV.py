class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        if not prerequisites:
            return [False] * len(queries)
        adj = [[] for _ in range(numCourses)]
        q = deque()

        for a, b in prerequisites:
            adj[a].append(b)

        def dfs(u, v):
            nonlocal visited
            visited.add(u)
            if u == v: return True
            for neighbor in adj[u]:
                if neighbor not in visited and dfs(neighbor, v): return True
            return False
        
        res = []
        for query in queries:
            u, v = query
            visited = set()
            if dfs(u, v): res.append(True)
            else: res.append(False)
        return res
        
