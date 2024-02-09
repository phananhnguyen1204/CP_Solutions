#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int n;
  cin >> n;
  vector<int> v(n);
  for(int i=0;i<n;i++){
    cin >> v[i];
  }
  int start =0;
  int end =n-1;
	while(start<n-1 && v[start]<v[start+1]){
    start++;
  }
  while(end >0 && v[end]>v[end-1]){
    end--;
  }
  if(start>end){
    cout << "yes" << endl;
    cout << 1 << " " << 1;
    return 0;
  }
  reverse(v.begin()+start,v.begin()+end+1);
  for(int i =0;i<n-1;i++){
    if(v[i]>=v[i+1]){
      cout << "no" <<endl;
      return 0;
    }
  }
  cout << "yes" << endl;
  cout << start +1 << " " << end+1;
  return 0;
}