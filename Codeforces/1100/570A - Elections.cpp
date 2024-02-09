#include <bits/stdc++.h>

using namespace std;

string s;
int n,m;

int main()
{
    cin >> n >> m;
    int mx = -1e9;
    int candidate = 0;
    vector<int>candidates(n,0);
    vector<vector<int>>matrix(m,vector<int>(n));
    for(int r = 0; r < m; r++){
        mx = -1e9;

        for(int c = 0; c < n; c++){
            cin >> matrix[r][c];
            if(mx < matrix[r][c]){
                mx = matrix[r][c];
                candidate = c;
            }
        }
        candidates[candidate]++;
    }
    int winner = -1;
    int res = -1;
    for(int i = 0; i < n; i++){
        if(winner < candidates[i]){
            winner = candidates[i];
            res = i;
        }
    }
    cout << res +1;

    return 0;
}
