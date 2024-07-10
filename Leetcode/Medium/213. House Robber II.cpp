class Solution
{
public:
    int rob(vector<int> &nums)
    {
        if (nums.size() == 1)
            return nums[0];
        return max(dp(nums, 0, nums.size() - 2), dp(nums, 1, nums.size() - 1));
    }

    int dp(vector<int> &nums, int start, int end)
    {
        int prev = nums[start];
        int second = 0;
        int res = nums[start];
        for (int i = start + 1; i <= end; i++)
        {
            res = max(second + nums[i], prev);
            second = prev;
            prev = res;
        }
        return res;
    }
};