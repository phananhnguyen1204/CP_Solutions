class Solution
{
public:
    string clearDigits(string s)
    {
        int n = s.length();
        string res = "";
        int cnt = 0;
        for (int i = n - 1; i >= 0; i--)
        {
            if (isdigit(s[i]))
            {
                cnt++;
            }
            else
            {
                if (cnt == 0)
                    res += s[i];
                else
                {
                    cnt--;
                }
            }
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
