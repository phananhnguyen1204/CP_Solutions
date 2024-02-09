#include <bits/stdc++.h>
#define ll long long


using namespace std;

ll k,n,w;

int main(){
  cin >> k >> n >> w;
  ll res = 0;
  for(auto i = 1; i <= w; i++){
    res += i*k;
  }
  if(res <= n){
    cout << 0;
  }
  else{
    cout << res - n;
  }
  
  
  
  return 0;
}