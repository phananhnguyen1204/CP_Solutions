#include<bits/stdc++.h>

using namespace std;

int main(){
  int k;
  cin >> k;
  vector<int> v(12);
  for(int i=0;i<12;i++){
    cin >> v[i];
  }
  sort(v.begin(),v.end(),greater<int>());
  int res = 0;
  for(int height: v){
    if(k<=0) break;
    res ++;
    k-=height;
    
  }
  cout << (k<=0 ? res: -1);
  return 0;
}