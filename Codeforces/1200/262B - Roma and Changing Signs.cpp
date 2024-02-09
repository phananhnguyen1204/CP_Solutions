#include <bits/stdc++.h>

using namespace std;

int n,k;

int main(){
  cin >> n >> k;
  int cnt_negative = 0;
  vector<int> v(n);
  int mx = 1e9;
  int idx = -1;
  for(int i = 0; i < n; i++){
    cin >> v[i];
    if(v[i] < 0 && cnt_negative != k){
      v[i] *= -1;
      cnt_negative++;
    }
    if(mx > v[i]){
      mx = v[i];
      idx = i;
    }
  }
  if((k - cnt_negative) %2 == 1){
    v[idx] *= -1;
  }
  long long res = 0;
  for(int i = 0; i < n; i++){
    res += v[i];
  }
  cout << res;
  
  
  return 0;
}