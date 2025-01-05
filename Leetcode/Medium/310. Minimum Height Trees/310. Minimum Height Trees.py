class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        adj = defaultdict(list)
        edge_cnt = [0] * n

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            edge_cnt[a] += 1
            edge_cnt[b] += 1
        
        leaves = deque()

        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)

        cnt_node = n

        while leaves:
            size = len(leaves)
            if cnt_node <= 2:
                break

            for i in range(size):
                node = leaves.popleft()
                edge_cnt[node] -= 1
                cnt_node -= 1

                for neighbor in adj[node]:
                    edge_cnt[neighbor] -= 1
                    if edge_cnt[neighbor] == 1:
                        leaves.append(neighbor)
        print(leaves)
        return list(leaves)



            