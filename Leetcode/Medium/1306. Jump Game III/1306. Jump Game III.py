class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        dirs = [-1, 1]
        visited = set()
        
        def dfs(i):
            if i < 0 or i >= n or i in visited:
                return False
            visited.add(i)
            if arr[i] == 0: return True
            
            for j in [i + arr[i], i - arr[i]]:
                if dfs(j):
                    return True
            
            return False

        return dfs(start)