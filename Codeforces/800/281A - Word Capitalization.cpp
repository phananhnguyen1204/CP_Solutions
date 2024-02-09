#include <bits/stdc++.h>

using namespace std;


string s;



int main()
{
    cin >> s;
    int n = s.length();
    if(n == 0){
        cout << "";
        return 0;
    }
    string res = (char)toupper(s[0]) + s.substr(1,n-1);
    cout << (res);
    return 0;
}
