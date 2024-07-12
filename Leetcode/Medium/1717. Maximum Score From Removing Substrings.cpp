class Solution
{
public:
    int res = 0;
    int maximumGain(string s, int x, int y)
    {
        // 'abba'
        // 'aba'
        // 'babbaba'
        // 'ababab'
        if (x > y)
        {
            string temp = solve(s, "ab", x);
            solve(temp, "ba", y);
        }
        else
        {
            string temp = solve(s, "ba", y);
            solve(temp, "ab", x);
        }
        return res;
    }

    string solve(string s, string remove_str, int point)
    {
        stack<char> st;
        for (char c : s)
        {
            if (!st.empty() && st.top() == remove_str[0] && c == remove_str[1])
            {
                st.pop();
                res += point;
            }
            else
            {
                st.push(c);
            }
        }
        string remain_string = "";
        while (!st.empty())
        {
            remain_string += st.top();
            st.pop();
        }
        reverse(remain_string.begin(), remain_string.end());
        return remain_string;
    }
};