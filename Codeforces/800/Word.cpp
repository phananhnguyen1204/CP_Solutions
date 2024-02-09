#include <bits/stdc++.h>
#define ll long long
#define MAX 1e9

using namespace std;


string s;



int main(){
    cin >> s;
    int countUpper = 0, countLower = 0;
    for(char c : s){
        if(isupper(c)){
            countUpper++;
        }
        else{
            countLower++;
        }
    }
    string res = "";
    bool changeToUpper = false;
    if(countUpper > countLower){
        changeToUpper = true;
    }
    
    for(char c : s){
        if(changeToUpper){
            res += toupper(c);
        }
        else{
            res += tolower(c);
        }
    }
    cout << res;

  return 0;
}