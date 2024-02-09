#include <bits/stdc++.h>

using namespace std;

char c;


int main()
{

    vector<vector<int>>grid(4,vector<int>(4,0));
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            cin >> c;
            if(c == '#'){
                grid[i][j] = 0;
            }
            else{
                grid[i][j] = 1;
            }
        }
        
    }
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            int sum = grid[i][j] + grid[i+1][j] + grid[i][j+1]+grid[i+1][j+1];
            if(sum != 2){
                cout << "YES";
                return 0;
            }
        }
    }
    cout << "NO";

    return 0;
}
