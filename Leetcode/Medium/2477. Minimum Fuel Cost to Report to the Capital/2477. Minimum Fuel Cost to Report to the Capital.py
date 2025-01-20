class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        """
        car require to reach a certain node >= ceil(representative / seat)
        minimum of feul = minimum of car 
        """

        if not roads: return 0

        res = 0
        visited = set()
        adj = defaultdict(list)
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            nonlocal res
            # count representative to reach current city
            people = 1
            visited.add(node)
            for next_city in adj[node]:
                if next_city not in visited:
                    people += dfs(next_city)

            if node != 0:
                res += int(ceil(people / seats))
            return people

        dfs(0)
        return res