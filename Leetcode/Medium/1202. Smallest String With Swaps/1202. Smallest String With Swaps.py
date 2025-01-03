class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)

        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])

            return parent[node]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return

            if rank[pa] > rank[pb]:
                parent[pb] = pa
            elif rank[pb] < rank[pa]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1

        for a, b in pairs:
            union(a, b)

        res = [""] * n
        hashmap = defaultdict(list)

        for i in range(n):
            parent_i = find(i)
            hashmap[parent_i].append(s[i])


        for key, value in hashmap.items():
            print(value)
            hashmap[key] = deque(sorted(value))
        
        for i in range(n):
            parent_i = find(i)
            res[i] = hashmap[parent_i].popleft()

        return "".join(res)


        


