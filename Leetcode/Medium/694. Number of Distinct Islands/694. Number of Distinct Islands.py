class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
        2 islands are the same if their dfs paths are the same
        """
        m, n = len(grid), len(grid[0])
        dirs = [[1, 0, "D"], [-1, 0, "U"], [0, 1, "L"], [0, -1, "R"]]

        unique_islands = set()
        visited = set()
        path = []

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        def dfs(r, c, direction, path):
            if not valid(r, c) or (r, c) in visited or grid[r][c] == 0: return 
            visited.add((r, c))
            path.append(direction)
            for dr, dc, new_direction in dirs:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, new_direction, path)
            path.append("0")
            

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    path = []
                    dfs(r, c, "0", path)
                    unique_islands.add("".join(path))           
        return len(unique_islands)
        