class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        visited = set()
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node): # the time needed to collect all apples in the subtrees and come back to this node
            time = 0
            visited.add(node)

            for child in adj[node]:
                if child in visited: continue
                child_time = dfs(child)
                if child_time != 0 or hasApple[child]:
                    time += 2 + child_time

            return time

        return dfs(0)