#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main(){
  int n;
  cin >> n;
  vector<pair<int,int>> v;
  int l,r;
  for(int i =0;i<n;i++){
    cin >> l >> r;
    v.push_back({l,r});
  }
  int start =v[0].first;
  int end = v[0].second;
  for(int i =0;i<n;i++){
    start = min(v[i].first,start);
    end = max(v[i].second,end);
  }
  for(int i =0;i<n;i++){
    if(start == v[i].first && end == v[i].second){
      cout << (i+1);
      return 0;
    }
  }
  cout << -1;
  return 0;
}