
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

string s;
int n;
unordered_map<string, int>freqs;

int main()
{
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> s;
        freqs[s]++;
    }
    int goals = -1e9;
    string res;
    for(auto [key,value] : freqs){
        if(value > goals){
            res  = key;
            goals =value;
        }
    }
    cout << res;

    return 0;
}
