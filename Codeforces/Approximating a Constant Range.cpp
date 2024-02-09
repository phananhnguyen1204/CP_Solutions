#include <bits/stdc++.h>

using namespace std;

unordered_map<int,int> freqs;

int main(){
  int n;
  cin >> n;
  vector<int> v(n);
  for(int i =0;i<n;i++){
    cin >> v[i];
  }
  int res =0;
  int start = 0;
  for(int end =0;end<n;end++){
    freqs[v[end]]++;
    while(freqs.size()>2){
      freqs[v[start]]--;
      if(freqs[v[start]]==0){
        freqs.erase(v[start]);
      }
      start++;
    }
    res = max(res,end-start+1);
  }
  cout << res;
  
  return 0;
}