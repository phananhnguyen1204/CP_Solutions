class Solution
{
public:
    int numberOfSubmatrices(vector<vector<char>> &grid)
    {
        int rows = grid.size();
        int cols = grid[0].size();

        vector<vector<int>> cntX(rows + 1, vector<int>(cols + 1, 0));
        vector<vector<int>> cntY(rows + 1, vector<int>(cols + 1, 0));

        for (int r = 1; r <= rows; r++)
        {
            for (int c = 1; c <= cols; ++c)
            {
                int addX = grid[r - 1][c - 1] == 'X';
                int addY = grid[r - 1][c - 1] == 'Y';
                cntX[r][c] = cntX[r - 1][c] + cntX[r][c - 1] - cntX[r - 1][c - 1] + addX;
                cntY[r][c] = cntY[r - 1][c] + cntY[r][c - 1] - cntY[r - 1][c - 1] + addY;
            }
        }

        int cnt = 0;
        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                if (cntX[r + 1][c + 1] == cntY[r + 1][c + 1] && cntX[r + 1][c + 1] != 0)
                {
                    cnt++;
                }
            }
        }

        return cnt;
    }
};