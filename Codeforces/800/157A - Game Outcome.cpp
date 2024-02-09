#include <bits/stdc++.h>

using namespace std;

int n;
int main()
{
    cin >> n;
    vector<vector<int>> grid(n, vector<int>(n));
    for(int r = 0 ; r < n; r++){
        for(int c = 0; c < n; c++){
            cin >> grid[r][c];
        }
    }
    vector<int>sum_row(n);
    for(int i = 0; i < n; i++){
        int sum = 0;
        for(int j = 0; j < n; j++){
            sum += grid[i][j];
        }
        sum_row[i] = sum;
    }
    
    vector<int> sum_col(n);
    for(int j = 0; j < n; j++){
        int sum = 0;
        for(int i = 0; i < n; i++){
            sum += grid[i][j];
        }
        sum_col[j] = sum;
    }
    int cnt = 0;
    for(int r = 0; r < n; r++){
        for(int c = 0; c < n; c++){
            if(sum_row[r] < sum_col[c]){
                cnt++;
            }
        }
    }
    cout << cnt;
    return 0;
}
