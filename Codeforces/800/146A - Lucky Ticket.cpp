#include <bits/stdc++.h>

using namespace std;

int n;
string s;

int main()
{
    
    cin >> n;
    cin >> s;
    int l_sum = 0, r_sum = 0;
    for(int i = 0; i < n/2; i++){
        if(s[i] != '4' && s[i] != '7'){
            cout << "NO";
            return 0;
        }
        l_sum += s[i] - '0';
    }
    
    for(int i = n/2; i < n; i++){
        if(s[i] != '4' && s[i] != '7'){
            cout << "NO";
            return 0;
        }
        r_sum += s[i] - '0';
    }
    cout << (r_sum == l_sum ? "YES" : "NO");

    return 0;
}
