class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        obstacleGrid[0][0] = 1

        for r in range(1, m):
            obstacleGrid[r][0] = 0 if ((obstacleGrid[r][0] == 1) or (obstacleGrid[r - 1][0] == 0)) else 1

        for c in range(1, n):
            obstacleGrid[0][c] = 0 if (obstacleGrid[0][c] == 1 or obstacleGrid[0][c - 1] == 0) else 1

        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]

        print (obstacleGrid)
        return obstacleGrid[m - 1][n - 1]
