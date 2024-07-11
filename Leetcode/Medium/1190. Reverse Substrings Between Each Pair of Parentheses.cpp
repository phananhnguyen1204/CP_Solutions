class Solution
{
public:
    string reverseParentheses(string s)
    {
        stack<char> st;
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] == ')')
            {
                string temp = "";
                while (!st.empty() && st.top() != '(')
                {
                    temp += st.top();
                    st.pop();
                }
                st.pop();
                for (int j = 0; j < temp.length(); j++)
                {
                    st.push(temp[j]);
                }
            }
            else
            {
                st.push(s[i]);
            }
        }
        string res = "";
        while (!st.empty())
        {
            res = st.top() + res;
            st.pop();
        }
        return res;
    }
};