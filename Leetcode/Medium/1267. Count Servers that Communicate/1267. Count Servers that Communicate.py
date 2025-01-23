class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        1 1 0 0 
        0 0 1 0
        0 0 1 0
        0 0 0 1

        rows = {
            0 : 2
            1 : 1
            2 : 1
            3 : 1
            
        }

        cols = {
            0 : 1
            1 : 1
            2 : 2
            3 : 1
        }
        """

        m, n = len(grid), len(grid[0])
        rows = defaultdict(int)
        cols = defaultdict(int)
        # row/col -> # of server

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        cnt = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (rows[r] > 1 or cols[c] > 1):
                    cnt += 1


        
        return cnt

        