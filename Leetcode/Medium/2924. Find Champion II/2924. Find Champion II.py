class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        cnt = 0
        res = -1
        for u, v in edges:
            indegree[v] += 1

        for i in range(n):
            if indegree[i] == 0:
                cnt += 1
                res = i

        return res if cnt == 1 else -1 