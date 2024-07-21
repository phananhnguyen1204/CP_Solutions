class Solution {
public:
    bool isVowel(char ch) {
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
}
    bool doesAliceWin(string s) {
        int n = s.length();
        int cnt = 0;
        
        for (int i = 0; i < n; ++i) {
            if (isVowel(s[i])) {
                cnt++;
            }
        }
        if(cnt == 0){
            return false;
        }
        return true;
    }
};