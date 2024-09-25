class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        '''
        2 -> 1 
        3 -> 4
        3 -> 2

        1: 1
        2: 2
        3: 2
        4: 1
        '''
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        root = None
        for key, val in graph.items():
            if len(val) == 1:
                root = key
                break
        visited = set()
        res = []
        def dfs(root):
            nonlocal res
            visited.add(root)
            res.append(root)
            for neighbor in graph[root]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(root)
        return res
        