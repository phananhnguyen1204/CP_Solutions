class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        """
        find max sum of roads between 2 pairs
        pair of ndoes can be not connected 
        """

        adj = defaultdict(list)
        indegree = defaultdict(int)
        nodes = set()
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
            nodes.add(a)
            nodes.add(b)
        nodes = list(nodes)
        res = 0
        print(indegree)
        print(nodes)
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                a, b = nodes[i], nodes[j]
                if a in adj[b] or b in adj[a]:
                    res = max(res, indegree[a] + indegree[b] - 1)
                else:
                    res = max(res, indegree[a] + indegree[b])
        return res