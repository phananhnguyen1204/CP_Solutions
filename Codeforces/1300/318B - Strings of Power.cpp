

#include <bits/stdc++.h>

using namespace std;

string s;

int main()
{
    cin >> s;
    int heavy =0;
    long long res = 0;
    int x = s.length() - 4;
    for(int i = 0; i < x ; i++){
        if(s.substr(i,5) == "heavy"){
            heavy++;
        }
        else if(s.substr(i,5) == "metal"){
            res += heavy;
        }
    }
    cout << res;
    

    return 0;
}
