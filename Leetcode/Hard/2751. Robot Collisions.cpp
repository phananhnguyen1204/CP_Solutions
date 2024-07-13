class Solution
{
public:
    vector<int> survivedRobotsHealths(vector<int> &positions, vector<int> &healths, string directions)
    {
        int n = positions.size();
        // to track the index
        // m will store index of each position coordinate
        unordered_map<int, int> m;
        for (int i = 0; i < n; i++)
        {
            m[positions[i]] = i;
        }
        sort(positions.begin(), positions.end());
        stack<int> s;
        for (auto position : positions)
        {
            int curr_index = m[position];
            if (directions[curr_index] == 'R')
            {
                s.push(curr_index);
            }
            else
            {
                while (!s.empty() && healths[curr_index] > 0)
                {
                    if (healths[curr_index] > healths[s.top()])
                    {
                        healths[curr_index]--;
                        healths[s.top()] = 0;
                        s.pop();
                    }
                    else if (healths[curr_index] < healths[s.top()])
                    {
                        healths[s.top()]--;
                        healths[curr_index] = 0;
                    }
                    else
                    {
                        healths[s.top()] = 0;
                        healths[curr_index] = 0;
                        s.pop();
                    }
                }
            }
        }
        vector<int> res;
        for (auto health : healths)
        {
            if (health > 0)
            {
                res.push_back(health);
            }
        }
        return res;
    }
};