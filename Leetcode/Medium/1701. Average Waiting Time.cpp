class Solution
{
public:
    double averageWaitingTime(vector<vector<int>> &customers)
    {
        double res = 0;
        int curr = 0;
        for (auto customer : customers)
        {
            curr = max(curr, customer[0]) + customer[1];
            res += curr - customer[0];
        }
        return res / customers.size();
    }
};