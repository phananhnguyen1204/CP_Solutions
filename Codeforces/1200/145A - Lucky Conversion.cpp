#include <bits/stdc++.h>

using namespace std;

string s,t;
int a,b;

int main()
{
    cin >> s >> t;
    for(int i = 0; i < s.length(); i++){
        if(s[i] != t[i]){
            if(s[i] == '4'){
                a++;
            }
            else{
                b++;
            }
        }
    }

    cout << max(a,b);
    return 0;
}
