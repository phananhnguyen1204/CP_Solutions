class Solution
{
public:
    int countCompleteDayPairs(vector<int> &hours)
    {
        int n = hours.size();
        int res = 0;
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                long long sum = hours[j] + hours[i];
                if (sum % 24 == 0)
                    res++;
            }
        }
        return res;
    }
};