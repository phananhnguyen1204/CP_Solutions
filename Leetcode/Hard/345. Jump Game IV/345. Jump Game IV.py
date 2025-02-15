class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return 0
        # mapping all index that has the same value
        values_map = defaultdict(list)
        for i in range(n):
            values_map[arr[i]].append(i)

        q = deque()
        q.append((0, 0))
        visited = set()
        visited.add(0)
        res = 0

        while q:
            i, dist = q.popleft()
            if i == n - 1: return dist
            for neighbor in [i - 1, i + 1]:
                if neighbor in visited: continue
                if 0 <= neighbor < n:
                    visited.add(neighbor)
                    q.append((neighbor, dist + 1))
            for neighbor in values_map[arr[i]]:
                if neighbor == i or neighbor in visited: 
                    continue
                visited.add(neighbor)
                q.append((neighbor, dist + 1))
            
            values_map[arr[i]] = []

        return -1