class Solution
{
public:
    vector<string> validStrings(int n)
    {
        vector<string> res;
        dfs(n, "", res);
        return res;
    }

    void dfs(int n, string curr, vector<string> &res)
    {
        if (curr.size() == n)
        {
            res.push_back(curr);
            return;
        }
        if (curr.empty() || curr.back() == '1')
        {
            dfs(n, curr + "0", res);
            dfs(n, curr + "1", res);
        }

        else
        {
            dfs(n, curr + "1", res);
        }
    }
};