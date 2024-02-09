

#include <bits/stdc++.h>

using namespace std;

int n,s;

int main()
{
    int cnt = 0;
    cin >> n >> s;
    vector<pair<int,int>> v(n);
    for(int i = 0; i < n; i++){
        cin >> v[i].first >> v[i].second;
    }
    
    int prev = s;
    for(int i = n-1; i >= 0; i--){
        cnt += (prev - v[i].first);
        if(v[i].second > cnt){
            cnt += (v[i].second - cnt);
        }
        prev = v[i].first;
    }
    cnt += prev;
    cout << cnt;
    return 0;
}
