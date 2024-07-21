class Solution {
public:
    int maxOperations(string s) {
        int res = 0;
        int cnt = 0;
        for(int i = 0; i < s.length(); i++){
            if(i > 0 && s[i] == '1' && s[i-1] == '0'){
                res += cnt;
            }
            if(s[i] == '1') cnt++;
        }
        if(s.back() == '0'){
            res += cnt;
        }
        return res;
    }
};