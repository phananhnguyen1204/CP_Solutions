class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x : x[0])
        
        parents = [i for i in range(n)]
        ranks = [1 for _ in range(n)]

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]

        def union(u, v):
            pu, pv = find(u), find(v)

            if pu == pv:
                return False
            
            if ranks[pu] > ranks[pv]:
                parents[pv] = pu
            elif ranks[pu] < ranks[pv]:
                parents[pu] = pv
            else:
                parents[pv] = pu
                ranks[pu] += 1
            return True

        cnt_group = n
        for timestamp, x, y in logs:
            if union(x, y):
                cnt_group -= 1

            if cnt_group == 1:
                return timestamp
        
        return -1
