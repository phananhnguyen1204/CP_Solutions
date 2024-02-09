#include <bits/stdc++.h>
#define MAX 3001

using namespace std;

int n,m,a,b;

int main(){
  cin >> n >> m;
  vector<int> problems(n);
	vector<int>prepare(m);
  for(int i = 0; i < n; i++){
    cin >> problems[i];
  }
  
  for(int i = 0; i < m; i++){
    cin >> prepare[i];
  }
  
  int res = 0;
  int i = 0, j = 0;
  while(i < n && j < m){
    if(prepare[j] >= problems[i]){
      res++;
      i++;
    }
    j++;
  }
  
  cout << n - res << endl;
  
  
  
  return 0;
}
