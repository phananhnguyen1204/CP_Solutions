#include <bits/stdc++.h>

using namespace std;

int n,k,x;

int main()
{
    cin >> n >> k;
    vector<pair<int,int>> v(n);
    for(int i =0 ; i < n; i++){
        cin >> x;
        v[i] = {x,i};
    }
    
    vector<int> res;
    sort(v.begin(), v.end());
    int cnt = 0;
    for(int i = 0; i < n; i++){
        cnt += v[i].first;
        if(cnt > k){
            break;
        }
        res.push_back(v[i].second);
    }
    cout << res.size() << endl;
    for(int i = 0; i < res.size(); i++){
        cout << res[i] + 1 << " ";
    }

    return 0;
}
