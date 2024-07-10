class Solution
{
public:
    int minCostClimbingStairs(vector<int> &cost)
    {
        int n = cost.size();
        int res = 0;
        int prev = 0;
        int second = 0;
        for (int i = 2; i < n + 1; i++)
        {
            res = min(prev + cost[i - 1], second + cost[i - 2]);
            second = prev;
            prev = res;
        }
        return res;
    }
};