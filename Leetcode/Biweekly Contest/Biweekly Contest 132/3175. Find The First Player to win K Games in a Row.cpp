class Solution
{
public:
    int findWinningPlayer(vector<int> &skills, int k)
    {
        int n = skills.size();
        if (k >= n)
            return max_element(skills.begin(), skills.end()) - skills.begin();
        deque<int> q;
        vector<int> cnt(n, 0);
        for (int i = 0; i < n; i++)
        {
            q.push_back(i);
        }
        int curr_winner = q.front();
        q.pop_front();
        while (true)
        {
            int challenger = q.front();
            q.pop_front();
            if (skills[challenger] < skills[curr_winner])
            {
                q.push_back(challenger);
                cnt[curr_winner]++;
            }
            else
            {
                q.push_back(curr_winner);
                curr_winner = challenger;
                cnt[curr_winner] = 1;
            }
            if (cnt[curr_winner] == k)
                return curr_winner;
        }
    }
};