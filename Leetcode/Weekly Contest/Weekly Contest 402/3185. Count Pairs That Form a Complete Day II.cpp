class Solution
{
public:
    long long countCompleteDayPairs(vector<int> &hours)
    {
        long long res = 0;
        unordered_map<int, int> cnt;
        for (auto hour : hours)
        {
            int curr_remainder = hour % 24;
            int res_remainder = (24 - curr_remainder) % 24;
            if (cnt[res_remainder] != 0)
            {
                res += cnt[res_remainder];
            }
            cnt[curr_remainder]++;
        }
        return res;
    }
};