
#include <bits/stdc++.h>
#define MAX 1e9 + 5
using namespace std;

long long n,value;
string grid[8];


int main()
{   
    int cnt_white =0, cnt_black = 0;
    unordered_map<char,int> values;
    values['Q'] = 9;
    values['R'] = 5;
    values['B'] = 3;
    values['N'] = 3;
    values['P'] = 1;
    values['K'] = 0;
    for(int i = 0;i < 8; i++){
        cin >> grid[i];
    }
    
    for(int r = 0; r < 8; r++){
        for(int c = 0; c < 8; c++){
            char x = grid[r][c];
            if(x != '.'){
                if(isupper(x)){
                    cnt_white += values[toupper(x)];
                }
                else{
                    cnt_black += values[toupper(x)];
                }
            }
        }
    }
    
    if(cnt_white > cnt_black){
        cout << "White";
    }
    else if(cnt_white < cnt_black){
        cout << "Black";
    }
    else{
        cout << "Draw";
    }



    

    return 0;
}
