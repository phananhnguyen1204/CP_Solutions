class Solution
{
public:
    string getSmallestString(string s)
    {
        for (int i = 1; i < s.size(); ++i)
        {
            if ((s[i] - '0') % 2 == (s[i - 1] - '0') % 2)
            { // Check if the parity is the same
                if (s[i] < s[i - 1])
                {
                    swap(s[i], s[i - 1]);
                    return s;
                }
            }
        }
        return s;
    }
};