class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
        cost[u] = max(cost[i] + time[u])
        need to finish all course v (prerequisite of u) before jumping to course u
        """

        cost = [0] * n
        indegree = [0] * n
        adj = defaultdict(list)

        for prev, next in relations:
            adj[prev-1].append(next-1)
            indegree[next-1] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0: q.append(i)

        res = 0

        while q:
            size = len(q)

            curr = q.popleft()
            res = max(cost[curr] + time[curr], res)
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                cost[neighbor] = max(cost[neighbor], cost[curr] + time[curr])
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return res