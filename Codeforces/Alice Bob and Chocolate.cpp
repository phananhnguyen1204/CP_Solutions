#include <iostream>
#include <vector>

using namespace std;

int main(){
  int n;
  cin >> n;
  vector<int> v(n);
  for(int i = 0; i < n; i++){
    cin >> v[i];
  }
  
  int l = 0, r = n-1;
  int l_time = 0, r_time = 0;
  int a = 0, b =0;
  while(l<=r){
		if(l_time + v[l] <= r_time + v[r]){
      l_time +=v[l];
      a++;
      l++;
    }
    else{
      r_time +=v[r];
      b++;
      r--;
    }
		
  }
  cout << a << " " << b;
  
  return 0;
}