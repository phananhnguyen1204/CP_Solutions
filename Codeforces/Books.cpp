#include <iostream>
#include <vector>

using namespace std;

int main(){
  int n,t;
  cin >> n >> t;
  vector<int> v(n);
  for(int i =0;i<n;i++){
    cin >> v[i];
  }
  int start =0;
  int sum = 0;
  int end = 0;
  while(end<n){
    sum+= v[end];
    if(sum>t){
      sum = sum - v[start];
      start++;
    }
    end++;
  }
  cout << end-start;
  return 0;
}