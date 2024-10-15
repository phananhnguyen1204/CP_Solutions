class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        n = len(isConnected)

        graph = defaultdict(list)
        for u in range(n):
            for v in range(n):
                if u != v:
                    if isConnected[u][v] == 1:
                        graph[u].append(v)
                        graph[v].append(u)

        visited = set()
        def dfs(u):
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v)


        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res

        

        