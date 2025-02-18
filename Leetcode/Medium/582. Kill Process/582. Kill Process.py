class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """
        tree based -> no cycle
        simulate tree representation?
        -> hashmap is enough 
        key: parent node
        value: list of all direct children
        """
        n = len(pid)
        adj = defaultdict(list)
        for i in range(n):
            parent = ppid[i]
            child = pid[i]
            if parent != 0:
                adj[parent].append(child)
        res = []
        def dfs(node):
            nonlocal res
            res.append(node)

            for next_node in adj[node]:
                dfs(next_node)

        dfs(kill)
        return res