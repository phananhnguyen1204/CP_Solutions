class Solution
{
public:
    long long maximumTotalDamage(vector<int> &power)
    {
        // Time Complexity: O(n)
        // Memory Limit Exceeded
        unordered_map<long long, long long> freq;
        long long minDamage = *min_element(power.begin(), power.end());
        long long maxDamage = *max_element(power.begin(), power.end());

        for (long long damage : power)
        {
            freq[damage]++;
        }

        if (freq.size() == 1)
            return minDamage * freq[minDamage];

        // vector<long long> dp(maxDamage - minDamage + 1, 0);
        // long long temp = minDamage; //to reduce the dp array size
        long long temp1 = minDamage * freq[minDamage];
        long long res = temp1;
        long long temp2;
        long long temp3;

        if (minDamage + 1 <= maxDamage)
        {
            temp2 = max(temp1, (minDamage + 1) * freq[minDamage + 1]);
            res = max(res, temp2);
        }

        if (minDamage + 2 <= maxDamage)
        {
            temp3 = max(max(temp1, temp2), (minDamage + 2) * freq[minDamage + 2]);
            res = max(res, temp3);
        }

        for (long long i = minDamage + 3; i <= maxDamage; i++)
        {
            long long temp = max(max(temp2, temp3), temp1 + i * freq[i]);
            res = max(res, temp);
            temp1 = temp2;
            temp2 = temp3;
            temp3 = temp;
        }

        return res;
    }
};
