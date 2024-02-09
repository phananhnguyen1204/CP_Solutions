#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
  int n;
  cin >> n;
  vector<int>v(n);
  vector<int> res(n);
  unordered_map<int,int> rank;
  
  for(int i =0;i<n;i++){
    cin >> v[i];
    res[i] = v[i];
  }
  sort(res.begin(),res.end(),greater<int>());
  for(int i =0;i<n;i++){
    int rate = res[i];
    if(rank.find(rate) == rank.end()){
      rank[rate] = i+1;
    }
  }
  for(int i =0;i<n;i++){
    cout << rank[v[i]] << " ";
  }
  
  
  
  
  return 0;
}