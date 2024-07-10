class Solution
{
public:
    int rob(vector<int> &nums)
    {
        if (nums.size() == 1)
            return nums[0];
        int prev = nums[0];
        int second = 0;
        int res = 0;
        for (int i = 1; i < nums.size(); i++)
        {
            res = max(prev, second + nums[i]);
            second = prev;
            prev = res;
        }
        return res;
    }
};