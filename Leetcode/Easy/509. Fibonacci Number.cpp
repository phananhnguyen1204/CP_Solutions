class Solution
{
public:
    int fib(int n)
    {
        if (n == 0)
            return 0;
        if (n == 1)
            return 1;
        int prev = 1, second = 0;
        int res = 0;
        for (int i = 2; i <= n; i++)
        {
            res = prev + second;
            second = prev;
            prev = res;
        }
        return res;
    }
};