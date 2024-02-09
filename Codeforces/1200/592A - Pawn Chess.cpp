#include <bits/stdc++.h>

using namespace std;

vector<string> matrix;

bool check_up( int row, int col){
    for(int i = row - 1; i >= 0; i--){
        if(matrix[i][col] == 'B'){
            return false;
        }
    }
    return true;
}

bool check_down( int row, int col){
    for(int i = row +1; i < 8; i++){
        if(matrix[i][col] == 'W'){
            return false;
        }
    }
    return true;
}
int main()
{
    matrix = vector<string>(8);
    for(int i = 0; i < 8; i++){
        cin >> matrix[i];
    }
    int white = 9;
    int black = 9;
    for(int r = 0; r < 8; r++){
        for(int c = 0; c < 8; c++){
            if(matrix[r][c] == 'W'){
                if(check_up(r,c)){
                    white = min(white, r);
                }
            }
            else if(matrix[r][c] == 'B'){
                if(check_down(r,c)){
                    black = min(black, 7 - r);
                }
            }
        }
    }
    cout << (white <= black ? "A" : "B");
    return 0;
}
