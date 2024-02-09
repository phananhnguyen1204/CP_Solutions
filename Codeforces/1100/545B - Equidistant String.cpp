#include <bits/stdc++.h>

using namespace std;


string s,t;
int main()
{
    
    cin >> s >> t;
    int cnt = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] != t[i]){
            cnt++;
        }
    }
    if(cnt %2 == 1){
        cout << "impossible";
        return 0;
    }
    else{
        cnt /= 2;
        string p;
        for(int i = 0; i < s.length(); i++){
            if(s[i] != t[i] && cnt > 0){
                p += 1 ^ s[i];
                cnt--;
            }
            else{
                p+=s[i];
            }
        }
        cout << p;
    }
    
    return 0;
}
