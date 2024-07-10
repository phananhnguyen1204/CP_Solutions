class Solution
{
public:
    int uniquePathsWithObstacles(vector<vector<int>> &obstacleGrid)
    {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        if (obstacleGrid[0][0] == 1 || obstacleGrid[m - 1][n - 1] == 1)
            return 0;
        obstacleGrid[0][0] = 1;
        for (int r = 1; r < m; r++)
        {
            obstacleGrid[r][0] = (obstacleGrid[r][0] == 0 && obstacleGrid[r - 1][0] == 1) ? 1 : 0;
        }
        for (int c = 1; c < n; c++)
        {
            obstacleGrid[0][c] = (obstacleGrid[0][c] == 0 && obstacleGrid[0][c - 1] == 1) ? 1 : 0;
        }
        for (int r = 1; r < m; r++)
        {
            for (int c = 1; c < n; c++)
            {
                if (obstacleGrid[r][c] == 1)
                {
                    obstacleGrid[r][c] = 0;
                }
                else
                {
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1];
                }
            }
        }
        return obstacleGrid[m - 1][n - 1];
    }
};