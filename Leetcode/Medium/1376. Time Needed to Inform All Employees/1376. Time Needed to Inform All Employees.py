class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        visited = set()
        q = deque()
        res = 0

        for i in range(n):
            if i != headID:
                adj[i].append(manager[i])
                adj[manager[i]].append(i)
        # current manager, time taken to inform all the above manager
        def dfs(manager, time):
            nonlocal res
            time += informTime[manager]
            res = max(time, res)
            visited.add(manager)

            for subordinate in adj[manager]:
                if subordinate not in visited:
                    dfs(subordinate, time)
            return time

        dfs(headID, 0)
        return res