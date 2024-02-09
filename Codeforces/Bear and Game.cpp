#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n,value;
  cin >> n;
  vector<int> v;
  for(int i = 0;i<n;i++){
    cin >> value;
    v.push_back(value);
  }
  
  int t =0;
  for(int i = 0;i<n;i++){
    if(t+15<v[i]){
      cout << t+15;
      return 0;
    }
    else{
      t = v[i];
    }
      
  }
  cout << min(t+15,90);
  return 0;
}