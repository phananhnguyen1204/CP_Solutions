class Solution
{
public:
    int minimumCost(int m, int n, vector<int> &horizontalCuts, vector<int> &verticalCuts)
    {
        sort(horizontalCuts.begin(), horizontalCuts.end(), greater<int>());
        sort(verticalCuts.begin(), verticalCuts.end(), greater<int>());

        int cnt_horizon = 1, cnt_vertical = 1;
        int res = 0;
        int i = 0, j = 0;

        while (i < horizontalCuts.size() && j < verticalCuts.size())
        {
            if (horizontalCuts[i] > verticalCuts[j])
            {
                res += horizontalCuts[i] * cnt_vertical;
                cnt_horizon++;
                i++;
            }
            else
            {
                res += verticalCuts[j] * cnt_horizon;
                cnt_vertical++;
                j++;
            }
        }

        while (i < horizontalCuts.size())
        {
            res += horizontalCuts[i] * cnt_vertical;
            i++;
        }

        while (j < verticalCuts.size())
        {
            res += verticalCuts[j] * cnt_horizon;
            j++;
        }

        return res;
    }
};