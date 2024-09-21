class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1] * n
        adj = [[] for _ in range(n)]
        q = deque()

        visited = set()
        for a,b in redEdges:
            adj[a].append((b, 0))
        
        for u, v in blueEdges:
            adj[u].append((v, 1))

        q.append((0, 0, -1))
        res[0] = 0
        visited.add((0, 0))
        visited.add((0, 1))
        while q:
            curr, dis, prev = q.popleft()
            for next_node, color in adj[curr]:
                if (next_node, color) not in visited and prev != color:
                    q.append((next_node, dis + 1, color))
                    #update one time
                    if res[next_node] == -1: res[next_node] = dis + 1
                    visited.add((next_node, color))
        return res
            
