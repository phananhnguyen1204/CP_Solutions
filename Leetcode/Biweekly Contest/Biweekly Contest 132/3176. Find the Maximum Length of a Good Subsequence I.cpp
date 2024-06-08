class Solution
{
public:
    int maximumLength(vector<int> &nums, int k)
    {
        int n = nums.size();
        if (n == 0)
            return 0;
        vector<vector<int>> dp(n, vector<int>(k + 1, 0));
        int res = 1;

        // Initialize the dp table
        for (int i = 0; i < n; ++i)
        {
            dp[i][0] = 1;
        }

        for (int i = 1; i < n; ++i)
        {
            for (int j = 0; j < i; ++j)
            {
                int changes = (nums[j] != nums[i]) ? 1 : 0;
                for (int prev = 0; prev + changes <= k; ++prev)
                {
                    dp[i][prev + changes] = max(dp[i][prev + changes], dp[j][prev] + 1);
                    res = max(res, dp[i][prev + changes]);
                }
            }
        }

        return res;
    }
};