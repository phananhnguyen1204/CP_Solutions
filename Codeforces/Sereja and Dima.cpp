#include <bits/stdc++.h>

using namespace std;

int main(){
  int n;
  cin >> n;
  vector<int>v(n);
  for(int i =0;i<n;i++){
    cin >> v[i];
  }
  int l =0;
  int r=n-1;
  int res1=0;
  int res2=0;
  bool player= true;
  while(l<=r){
    if(v[r]>v[l]){
      if(player){
        res1+=v[r];
      }
      else{
        res2+=v[r];
      }
      r--;
    }
    else{
       if(player){
        res1+=v[l];
      }
      else{
        res2+=v[l];
      }
      l++;
    }
    player =!player;
  }
  cout << res1 << " " << res2;
  return 0;
}