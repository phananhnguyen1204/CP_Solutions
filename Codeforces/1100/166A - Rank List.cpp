#include <bits/stdc++.h>

using namespace std;

int n,k,p,t;

bool option(pair<int,int> p1, pair<int,int> p2){
    return p1.first > p2.first || (p1.first == p2.first && p1.second < p2.second);
}

int main()
{
    cin >> n >> k;
    vector<pair<int,int>> v(n);
    for(int i = 0; i < n; i++){
        cin >> v[i].first >> v[i].second;
    }
    sort(v.begin(),v.end(),option);
    int res = 0;
    for(auto x: v){
        if(x == v[k-1]){
            res++;
        }
    }
    cout << res;
    return 0;
}
