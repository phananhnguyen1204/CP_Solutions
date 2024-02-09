#include <bits/stdc++.h>

using namespace std;

int n,x,y;

int main()
{
    cin >> n;
    if(n == 1){
        cout << 1;
        return 0;
    }
    vector<vector<int>> matrix(n,vector<int>(n));
    vector<long long> row(n,0);
    vector<long long> col(n,0);
    long long diagnal1 = 0, diagnal2 = 0;
    for(int r = 0; r < n; r++){
        for(int c = 0; c < n; c++){
            cin >> matrix[r][c];
            row[r] += matrix[r][c];
            col[c] += matrix[r][c];
            if(r == c){
                diagnal1 += matrix[r][c];
            }
            if(c == n-r-1){
                diagnal2 += matrix[r][c];
            }
            if(matrix[r][c] == 0){
                x = r;
                y = c;
            }
        }
    }
    long long sum = x == 0 ? row[1] : row[0];
    for(int i = 0; i < n; i++){
        if(i != x && row[i] != sum){
            cout << -1;
            return 0;
        }
    }
    
    for(int c = 0; c < n; c++){
        if(c != y && col[c] != sum ){
            cout << -1;
            return 0;
        }
    }
    if((x != y && diagnal1 != sum) || (x != n-1-y && diagnal2 != sum)){
        cout << -1;
        return 0;
    }
    if(row[x] != col[y] || (x == y && diagnal1 != row[x]) || (x == n-1-y && diagnal2 != row[x])){
        cout << -1;
        return 0;
    }
    if(row[x] < sum){
        cout << sum - row[x];
    }
    else{
        cout << -1;
    }
    

    return 0;
}
