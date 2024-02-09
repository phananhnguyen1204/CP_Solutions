#include <bits/stdc++.h>

using namespace std;

int n;
vector<vector<int>> grid;
unordered_set<int> s;

int main()
{
    cin >> n;
    grid = vector<vector<int>>(n, vector<int>(n));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> grid[i][j];
            if(grid[i][j] != -1){
                if(grid[i][j] == 1){
                    s.insert(i + 1);
                }
                else if(grid[i][j] == 2){
                    s.insert(j+1);
                }
                else if( grid[i][j] == 3){
                    s.insert(i+1);
                    s.insert(j+1);
                }
            }
        }
    }
    cout << (n - s.size()) << endl;
    for(int i = 1; i <= n; i++){
        if(s.find(i) == s.end()){
            cout << i << " ";
        }
    }

    return 0;
}
