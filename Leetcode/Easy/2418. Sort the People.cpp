class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<pair<int,string>> m;
        for(int i = 0; i < names.size();i++){
            m.push_back({heights[i], names[i]});
        }
        sort(m.begin(), m.end(), greater<pair<int,string>>());
        vector<string> res;
        for(int i = 0; i < names.size(); i++){
            res.push_back(m[i].second);
        }
        return res;
    }
};