class Solution
{
public:
    int climbStairs(int n)
    {
        if (n == 1 || n == 2)
            return n;
        int prev = 2, second = 1;
        int res = 0;
        for (int i = 3; i <= n; i++)
        {
            res = prev + second;
            second = prev;
            prev = res;
        }
        return res;
    }
};