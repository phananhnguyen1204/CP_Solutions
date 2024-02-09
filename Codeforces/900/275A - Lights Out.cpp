#include <bits/stdc++.h>

using namespace std;

int n;
string s;

bool valid(int r, int c){
    return r >= 0 && r <3 && c >=0 && c < 3;
}

int main()
{
    vector<vector<int>> grid(3,vector<int>(3));
    vector<vector<int>> res(3,vector<int>(3,1));
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cin >> grid[i][j];
        }
    }
    for(int r = 0; r < 3; r++){
        for(int c = 0; c < 3; c++){
            if(grid[r][c] %2 ==1){
                res[r][c] ^= 1;
                if(valid(r+1,c)){
                    res[r+1][c] ^= 1;
                }
                if(valid(r,c+1)){
                    res[r][c+1] ^= 1;
                }
                if(valid(r-1,c)){
                    res[r-1][c] ^= 1;
                }
                if(valid(r,c-1)){
                    res[r][c-1] ^= 1;
                }
            }
        }
    }
    
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cout << res[i][j];
        }
        cout << endl;
    }
    return 0;
}
