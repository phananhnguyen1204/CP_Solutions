#include <bits/stdc++.h>

using namespace std;

int sr,sc,er,ec;

bool check_diagnal(int r1, int c1, int r2, int c2){
    return abs(r2 - r1) == abs(c2 - c1);
}

int main()
{
    cin >> sr >> sc >> er >> ec;
    if(sr == er || sc == ec){
        cout << 1;
    }
    else{
        cout << 2;
    }
    cout << " ";
    if(((sr+sc) % 2) != ((er+ec)%2)){
        cout << 0;
    }
    else{
        if(check_diagnal(sr,sc,er,ec)){
            cout << 1;
        }
        else{
            cout << 2;
        }
    }
    cout << " ";
    cout << max(abs(ec-sc),abs(sr-er));
    
    
    

    return 0;
}
