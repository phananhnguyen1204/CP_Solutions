#include <bits/stdc++.h>

using namespace std;

int n;

int main(){
  
  cin >> n;
  vector<int> v(n);
  for(int i = 0; i < n; i++){
    cin >> v[i];
  }
  sort(v.begin(), v.end());
  int res = 1;
  for(int i = 0; i < n; i++){
    int value = v[i] + 5;
    int len = upper_bound(v.begin(), v.end(),value) - v.begin() - i;
		res = max(res, len);
  }
  cout << res;
  
  return 0;
}