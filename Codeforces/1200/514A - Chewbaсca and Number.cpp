#include <bits/stdc++.h>

using namespace std;


string s;
int main()
{
    cin >> s;
    string res;
    for(int i =0; i < s.length(); i++){
        int value = s[i] - '0';
        if(value > 9 - value ){
            if(i == 0 && value == 9){
                res += s[i];
            }
            else{
                res += (char)(9 - value + '0');
            }
        }
        else{
            res += s[i];
        }
    }
    cout << res;
    
    
    return 0;
}
