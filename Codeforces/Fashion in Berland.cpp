#include <vector>
#include <iostream>
using namespace std;

bool sol(vector<int>& v,int n){
  if(v.size()==1){
    return v[0] == 1;
  }
  int cnt = 0;
 	for(int i =0;i<n;i++){
    if(v[i] == 0){
      cnt++;
    }
  }
	return cnt == 1;
}

int main(){
	int n,value;
  cin >> n;
  vector<int> v;
  for(int i =0;i<n;i++){
    cin >> value;
    v.push_back(value);
  }
  bool res = sol(v,n);
  if(res )
    cout << "YES";
  else
    cout << "NO";
  return 0;
}
