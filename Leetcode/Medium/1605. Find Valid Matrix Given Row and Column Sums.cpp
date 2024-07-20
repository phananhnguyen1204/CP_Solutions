class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        int m = rowSum.size();
        int n = colSum.size();
        vector<int> currRow(m,0);
        vector<int> currCol(n,0);
        vector<vector<int>> res(m, vector<int>(n,0));
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                res[i][j] = min(rowSum[i] - currRow[i], colSum[j]-currCol[j]);
                currRow[i] += res[i][j];
                currCol[j] += res[i][j];
            }
        }
        return res;
    }
};