#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int n,x;
  cin >> n >> x;
  vector<int> v(n);
  for(int i=0;i<n;i++){
    cin >> v[i];
  }
  sort(v.begin(),v.end());
  long long res = 0;
  for(int i =0;i<n;i++){
    res += 1LL * v[i] * x;
    if(x>1){
      x--;
    }
  }
  cout << res;
  
  
  return 0;
}