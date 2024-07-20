class Solution {
public:
    vector<vector<int>> dp;
    int minDifficulty(vector<int>& jobDifficulty, int d) {
        //dp[d][i] = dp[d+1][j] + min(max(jobDifficulty[i->j-1]))
        dp = vector<vector<int>> (jobDifficulty.size(),vector<int>(d+1,-1));
        if(d > jobDifficulty.size()){
            return -1;
        }

        return dfs(jobDifficulty, d, 1, 0);
    }

    int dfs(vector<int>& jobDifficulty, int d, int curr_day, int curr_index){
        if(dp[curr_index][curr_day] != -1){
            return dp[curr_index][curr_day];
        }
        //last 
        if(curr_day == d){
            int res = 0;
            for(int j = curr_index; j < jobDifficulty.size();j++){
                res = max(jobDifficulty[j],res);
            }
            return res;
        }
        // cout << "curr_index: " << curr_index << " " << endl;
        // cout << " curr_day: " << curr_day << endl;

        //remaining day
        int day_remain = d - curr_day;
        //minimum job difficulty if we are starting at curr_indexth job and at curr_day
        int res = 1e9;
        int daily_max_job = -1e9;
        for(int j = curr_index; j < jobDifficulty.size() - day_remain; j++){
            daily_max_job = max(daily_max_job, jobDifficulty[j]);
            res = min(res, daily_max_job + dfs(jobDifficulty, d,curr_day+1,j+1));
        }
         dp[curr_index][curr_day] = res;
         return res;
    }
};