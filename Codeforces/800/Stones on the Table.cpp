#include <bits/stdc++.h>
#define ll long long
#define MAX 1e9

using namespace std;


int n;
string s;

int main(){
    cin >> n;
    cin >> s;
    int res = 0;
    for(int i = 0; i < n-1; i++){
        if(s[i] == s[i+1]){
            res++;
        }
    }
    cout << res;

  return 0;
}