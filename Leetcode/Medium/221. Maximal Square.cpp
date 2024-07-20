class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int res = 0;
        vector<vector<int>> dp(m+1, vector<int>(n+1,0));
        for(int i = 1; i < m+1; i++){
            for(int j = 1; j < n+1; j++){
                if(matrix[i-1][j-1] == '1'){
                    dp[i][j] = min(dp[i-1][j], min(dp[i-1][j-1], dp[i][j-1])) + 1;
                    res = max(res,dp[i][j] * dp[i][j]);
                }
            }
        }
        return res;
    }
};