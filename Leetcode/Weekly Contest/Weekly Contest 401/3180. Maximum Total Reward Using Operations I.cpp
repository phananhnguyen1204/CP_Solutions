class Solution
{
public:
    vector<vector<int>> dp;
    int dfs(vector<int> &rewardValues, int x, int index)
    {
        if (index >= rewardValues.size())
            return x;
        if (dp[index][x] != -1)
            return dp[index][x];
        int exclude = dfs(rewardValues, x, index + 1);
        int include = 0;
        // only take if current reward > current x
        if (rewardValues[index] > x)
        {
            include = dfs(rewardValues, x + rewardValues[index], index + 1);
        }
        dp[index][x] = max(exclude, include);
        return dp[index][x];
    }

    int maxTotalReward(vector<int> &rewardValues)
    {
        sort(rewardValues.begin(), rewardValues.end());
        // Got Memory Limit Exceeded at first with this
        // int sum = accumulate(rewardValues.begin(), rewardValues.end(),0);
        // dp = vector<vector<int>>(rewardValues.size(),vector<int>(sum,-1));
        // Optimize:
        int maxi = *max_element(rewardValues.begin(), rewardValues.end());
        dp = vector<vector<int>>(rewardValues.size(), vector<int>(2 * maxi, -1));
        return dfs(rewardValues, 0, 0);
    }
};