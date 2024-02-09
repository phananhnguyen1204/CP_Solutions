#include <bits/stdc++.h>

using namespace std;

int n,m,h;


int main()
{
    cin >> n;
    vector<vector<int>> cnt(24,vector<int>(60,0));
    for(int i = 0; i < n; i++){
        cin >> h >> m;
        cnt[h][m]++;
        
    }
    int res = -1;
    for(int i = 0; i < 24; i++){
        for(int j = 0; j < 60; j++){
            res = max(res, cnt[i][j]);
        }
    }
    cout << res;

    return 0;
}
