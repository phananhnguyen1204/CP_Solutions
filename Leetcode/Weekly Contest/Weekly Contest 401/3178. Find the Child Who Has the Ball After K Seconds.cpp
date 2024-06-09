class Solution
{
public:
    int numberOfChild(int n, int k)
    {
        int it = 0;
        bool right = true;
        for (int i = 0; i < k; i++)
        {
            if (right)
            {
                it++;
            }
            else
            {
                it--;
            }
            if (it == n - 1)
            {
                right = false;
            }
            if (it == 0)
            {
                right = true;
            }
        }
        return it;
    }
};