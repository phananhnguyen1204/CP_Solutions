#include <bits/stdc++.h>

using namespace std;

string s;

int main()
{
    
    cin >> s;
    unordered_map<char,int> freqs;
    for(char c: s){
        if(c == '4' || c == '7'){
            freqs[c]++;
        }
    }
    if(freqs.size() == 0){
        cout << -1;
    }
    else{
        if(freqs['4'] >= freqs['7']){
            cout << 4;
        }
        else{
            cout << 7;
        }
    }


    return 0;
}
