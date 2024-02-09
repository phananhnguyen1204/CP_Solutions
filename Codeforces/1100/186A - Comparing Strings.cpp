
#include <bits/stdc++.h>
#define MAX 1e9 + 5
using namespace std;

string s,t;


int main()
{
    cin >> s >> t;
    if(s.length() != t.length()){
        cout << "NO";
        return 0;
    }
    unordered_map<int,int> freqs;
    int cnt = 0;
    for(int i = 0; i < s.length(); i++){
        freqs[s[i]]++;
        freqs[t[i]]--;
        if(s[i] != t[i]){
            cnt++;
        }
    }
    for(auto [key,value]: freqs){
        if(value != 0){
            cout << "NO";
            return 0;
        }
    }
    cout << (cnt == 2 ? "YES" : "NO");

    

    return 0;
}
