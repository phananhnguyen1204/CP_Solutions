class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Color the graph, 
        # color = {
        #.   -1: 1st group
        #.    0: not visited yet
        #.    1: 2nd group   
        #}
        """
        graph might not connected -> run a loop from each node
        bipartite -> no odd-length cycle
        """

        n = len(graph)

        visited = defaultdict(int)

        def dfs(i, color):
            if visited[i] != 0:
                # if node is visited
                # and their assigned color is different 
                # return False -> it is not bipartite
                return visited[i] == color
            visited[i] = color
            color *= -1
            for neighbor in graph[i]:
                if not dfs(neighbor, color):
                    return False

            return True

        for i in range(n):
            if visited[i] == 0 and not dfs(i, -1):
                return False

        return True
            

        