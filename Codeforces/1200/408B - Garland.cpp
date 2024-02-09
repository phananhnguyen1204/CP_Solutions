#include <bits/stdc++.h>

using namespace std;


string s,t;
int main()
{
    cin >> s >> t;
    vector<int> freqs1(26,-1);
    vector<int> freqs2(26,-1);
    for(char c: s){
        if(freqs1[c - 'a'] != -1){
            freqs1[c-'a']++;
        }
        else{
            freqs1[c-'a'] = 1;
        }
    }
    for(char c: t){
        if(freqs2[c - 'a'] != -1){
            freqs2[c-'a']++;
        }
        else{
            freqs2[c-'a'] = 1;
        }
    }
    int res = 0;
    for(int i = 0; i < 26; i++){
        if(freqs2[i] != -1 && freqs1[i] == -1){
            cout << -1;
            return 0;
        }
        else if(freqs2[i] != -1 &&freqs1[i]!= -1){
            res += min(freqs2[i],freqs1[i]);
        }
    }
    cout << res;
    
    
    return 0;
}
