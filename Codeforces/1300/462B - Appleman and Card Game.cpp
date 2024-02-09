#include <bits/stdc++.h>

using namespace std;

long long n,k;
string s;


int main()
{
    unordered_map<char,long long> freqs;
    cin >> n >> k;
    cin >> s;
    for(char c: s){
        freqs[c]++;
    }
    vector<long long> v;
    for(auto it = freqs.begin(); it != freqs.end(); it++){
        v.push_back(it->second);
    }
    sort(v.begin(),v.end(),greater<int>());
    long long res = 0;
    for(auto x: v){
        if(x < k){
            res += x*x;
            k -= x;
        }
        else{
            res += k*k;
            break;
        }
    }
    cout << res;

    return 0;
}
