class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        brute force, for every 0 cell, do bfs/dfs to calculate area -> get max area -> (m^2 * n^2)

        precompute area -> use hashmap island -> area -> O(m * n)
        """
        m, n = len(grid), len(grid[0])
        
        res = 0
        island_mapping = defaultdict(int)
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def calculate_area():
            group_island = 2
            seen = set()
            area = 0
            nonlocal res

            def dfs(r, c):
                nonlocal group_island, area
                grid[r][c] = group_island
                area += 1
                seen.add((r, c))
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] == 1:
                        dfs(nr, nc)
            
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1 and (r, c) not in seen:
                        area = 0
                        dfs(r, c)
                        island_mapping[group_island] = area
                        res = max(res, area)
                        group_island += 1

        calculate_area()
        print(grid)
        
        island_visited = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    island_visited = set()
                    total_area = 1
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] not in island_visited:
                            area = island_mapping[grid[nr][nc]]
                            total_area += area
                            island_visited.add(grid[nr][nc])

                    res = max(res, total_area)

        return res
                    
                        

        

        
        