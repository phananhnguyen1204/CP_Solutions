#include <bits/stdc++.h>

using namespace std;

int n;
vector<string> grid;
int main()
{
    cin >> n;
    grid = vector<string>(n);
    for(int i = 0; i < n; i++){
        cin >> grid[i];
    }
    
    unordered_set<char> diagonal;
    unordered_set<char> seen;
    for(int r = 0; r < n; r++){
        diagonal.insert(grid[r][r]);
        if(diagonal.size() > 1){
            cout << "NO";
            return 0;
        }
    }
    for(int r = 0; r < n; r++){
        diagonal.insert(grid[r][n-1-r]);
        if(diagonal.size() > 1){
            cout << "NO";
            return 0;
        }
    }
    
    for(int r = 0; r < n; r++){
        for(int c = 0; c < n; c++){
            if(r == c || (c == n - 1 - r)){
                continue;
            }
            if(diagonal.find(grid[r][c]) != diagonal.end()){
                cout << "NO";
                return 0;
            }
            seen.insert(grid[r][c]);
            if(seen.size() > 1){
                cout << "NO";
                return 0;
            }
        }
    }
    cout << "YES";
    

    return 0;
}
