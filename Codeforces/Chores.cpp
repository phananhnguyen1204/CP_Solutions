#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int n,a,b;
  cin >> n >> a >> b;
  vector<int> v(n);
  for(int i =0;i<n;i++){
    cin >> v[i];
  }
  sort(v.begin(),v.end());
	long long low = v[b-1];
  long long high = v[b];
  if(low == high) cout << 0;
  else cout << high - low;
  
  return 0;
}