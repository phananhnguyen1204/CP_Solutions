class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        total = 0
        res = 0
        visited = set()
        adj = [[] for _ in range(len(bombs))]

        def dist(x1, y1, x2, y2):
            return (y1 - y2) ** 2 + (x1 - x2) ** 2
        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            for j in range(len(bombs)):
                if i == j: continue
                x2, y2, r2 = bombs[j]
                if dist(x1, y1, x2, y2) <= r1 ** 2:
                    adj[i].append(j)
                    # adj[j].append(i)

        def dfs(idx):
            visited.add(idx)
            nonlocal total
            total += 1
            for nextIdx in adj[idx]:
                if nextIdx not in visited:
                    dfs(nextIdx)
        
        for i in range(len(bombs)):
            visited = set()
            total = 0
            dfs(i)
            res = max(total, res)
        return res