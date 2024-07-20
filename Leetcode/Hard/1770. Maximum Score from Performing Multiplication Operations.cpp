class Solution {
public:
    vector<vector<int>> dp;
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        dp = vector<vector<int>>(nums.size()+1, vector<int>(multipliers.size()+1,1e9));
        return dfs(nums,multipliers, 0, 0);
    }

    int dfs(vector<int>& nums, vector<int>& multipliers, int l, int opt){
        if(opt >= multipliers.size()){
            return 0;
        }
        if(dp[l][opt] != 1e9){
            return dp[l][opt];
        }
        int left = multipliers[opt] * nums[l] + dfs(nums,multipliers,l+1,opt+1);
        int r = nums.size() - 1 - (opt - l);
        int right = multipliers[opt] * nums[r] + dfs(nums,multipliers, l, opt+1);
        dp[l][opt] = max(left,right);
        return dp[l][opt];
    }
};