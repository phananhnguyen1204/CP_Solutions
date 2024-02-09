#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main(){
  int n;
  cin >> n;
  vector<int> v(n);
  unordered_map<int,int> freqs;
  for(int i=0;i<n;i++){
    cin >> v[i];
    freqs[v[i]]++;
  }
  int largest = 0;
  for(auto [key,value]: freqs){
    largest = max(largest,value);
  }
  cout << largest << " "<< freqs.size();
  return 0;
  
  
  
}