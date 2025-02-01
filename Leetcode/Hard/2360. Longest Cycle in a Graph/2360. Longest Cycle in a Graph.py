class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        """
        directed graph
        distance between 2 nodes a, b = dist[b] - dist[a] + 1
        go to every node
        have visited set() to avoid traverse nodes multiple times O(n^2) -> O(n)
        path hashmap -> to keep track of the cycle and depth of each node
        """

        visited = set()
        depth = defaultdict(int)
        res = -1 # no cycle exists

        def dfs(node):
            nonlocal res
            neighbor = edges[node]
            visited.add(node)
            
            # foudn cycle
            if neighbor != -1 and neighbor in depth:
                res = max(res, depth[node] - depth[neighbor] + 1)
            # node have not been processed
            elif neighbor != -1 and neighbor not in visited:
                depth[neighbor] = depth[node] + 1
                dfs(neighbor)
        

        n = len(edges)
        for i in range(n):
            # don't repeat computation
            if i not in visited:
                depth = defaultdict(int)
                depth[i] = 1
                dfs(i)

        return res

