class Solution
{
public:
    long long minimumCost(int m, int n, vector<int> &horizontalCut, vector<int> &verticalCut)
    {
        sort(horizontalCut.begin(), horizontalCut.end(), greater<int>());
        sort(verticalCut.begin(), verticalCut.end(), greater<int>());

        int cnt_horizon = 1, cnt_vertical = 1;
        long long res = 0;
        int i = 0, j = 0;

        while (i < horizontalCut.size() && j < verticalCut.size())
        {
            if (horizontalCut[i] > verticalCut[j])
            {
                res += horizontalCut[i] * cnt_vertical;
                cnt_horizon++;
                i++;
            }
            else
            {
                res += verticalCut[j] * cnt_horizon;
                cnt_vertical++;
                j++;
            }
        }

        while (i < horizontalCut.size())
        {
            res += horizontalCut[i] * cnt_vertical;
            i++;
        }

        while (j < verticalCut.size())
        {
            res += verticalCut[j] * cnt_horizon;
            j++;
        }

        return res;
    }
};