#include <bits/stdc++.h>
#define ll long long

using namespace std;

int n,t;
string s;



int main(){
    cin >> n >> t;
    cin >> s;
    while(t--){
        for(int i = 0; i < n-1; i++){
            if(s[i] == 'B' && s[i+1] == 'G'){
                swap(s[i],s[i+1]);
                i++;
            }
        }
    }
    cout << s << endl;

  
  return 0;
}