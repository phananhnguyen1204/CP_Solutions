class Solution
{
public:
    int valueAfterKSeconds(int n, int k)
    {
        int MOD = 1e9 + 7;
        vector<int> res(n, 1);
        for (int i = 1; i <= k; i++)
        {
            vector<long long> prefix_sum(n, 0);
            prefix_sum[0] = res[0];
            for (int i = 1; i < n; i++)
            {
                prefix_sum[i] = (prefix_sum[i - 1] + res[i]) % MOD;
            }

            for (int i = 0; i < n; i++)
            {
                res[i] = prefix_sum[i];
            }
        }

        return res[n - 1];
    }
};