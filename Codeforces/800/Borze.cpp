#include <bits/stdc++.h>
#define ll long long

using namespace std;


string s;



int main(){
    cin >> s;
    string res = "";
    for(int i = 0; i < s.length() ; i++){
        if(s[i] == '-'){
            if(s[i+1] == '-'){
                res += "2";
            }
            else{
                res += "1";
            }
            i++;
        }
        else{
            res += "0";
        }
    }
    cout << res;

  
  return 0;
}