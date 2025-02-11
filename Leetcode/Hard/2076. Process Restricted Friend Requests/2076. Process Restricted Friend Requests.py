class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        """
        a want to make friend with b
        
        c can not be friend with d
        if a and c are on the same group and b and d are one the same group -> a can not make friend with b
        if a and d are on the same group and b and c are one the same group -> a can not make friend with b
        """

        parent = [i for i in range(n)]
        res = []
        rank = [1 for _ in range(n)]
        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv: # already friend
                return
            if rank[pu] > rank[pv]:
                parent[pv] = pu
            elif rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                rank[pu] += 1
                parent[pv] = pu
        for a, b in requests:
            pa, pb = find(a), find(b)
            if pa == pb: # aready friend:
                res.append(True)
                continue
            can_make_friend = True
            for c, d in restrictions:
                pc, pd = find(c), find(d)
                if pa == pc and pb == pd:
                    can_make_friend = False
                    break
                if pa == pd and pb == pc:
                    can_make_friend = False
                    break
            if can_make_friend: 
                union(a, b)
                res.append(True)
            else: res.append(False)
        return res

        