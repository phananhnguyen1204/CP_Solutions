
#include <bits/stdc++.h>

using namespace std;

int s,n;
int strength, bonus;

int main()
{
    vector<pair<int,int>> v;
    cin >> s >> n;
    v = vector<pair<int,int>>(n);
    for(int i = 0; i < n; i++){
        cin >> strength >> bonus;
        v[i].first = strength;
        v[i].second = bonus;
    }
    
    sort(v.begin(), v.end());
    for(int i = 0 ; i < (int)v.size(); i++){
        if(s <= v[i].first){
            cout << "NO" << endl;
            return 0;
        }
        else{
            s += v[i].second;
        }
    }
    cout << " YES" << endl;

    return 0;
}
