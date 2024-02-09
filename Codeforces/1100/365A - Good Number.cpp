
#include <bits/stdc++.h>

using namespace std;

int n,k;
string s;

int main()
{
    cin >> n >> k;
    int res = 0;
    for(int i = 0; i < n; i++){
        cin >> s;
        int cnt = 0;
        unordered_set<char> seen;
        for(char c: s){
            if(c - '0' <= k){
                seen.insert(c);
            }
        }
        if(seen.size() == k+1){
            res++;
        }
    }
    cout << res;

    return 0;
}
