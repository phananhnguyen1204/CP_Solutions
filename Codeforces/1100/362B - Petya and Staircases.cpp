
#include <bits/stdc++.h>

using namespace std;

int n,m;

int main()
{
    cin >> n >> m;
    vector<int>v (m);
    for(int i = 0; i < m; i++){
        cin >> v[i];
        if(v[i] == n || v[i] == 1){
            cout << "NO";
            return 0;
        }
    }
    sort(v.begin(), v.end());
    for(int i = 0; i < min(v.size(), v.size() - 2); i++){
        if(v[i] +1 == v[i+1] && v[i+1] + 1 == v[i+2]){
            cout << "NO";
            return 0;
        }
    }
    cout << "YES";

    return 0;
}
