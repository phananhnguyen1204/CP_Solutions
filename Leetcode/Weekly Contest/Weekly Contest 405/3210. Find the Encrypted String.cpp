class Solution
{
public:
    string getEncryptedString(string s, int k)
    {
        string res = "";
        for (int i = 0; i < s.length(); i++)
        {
            res += s[(i + k) % s.length()];
        }
        return res;
    }
};