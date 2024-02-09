#include <bits/stdc++.h>

using namespace std;

int n,m,x,y,k;

int main(){
  cin >> n >> m >> x >> y; 
  vector<int> soldiers(n);
  vector<int> vests(m);
  
  for(int i = 0; i < n; i++){
    cin >> soldiers[i];
  }
  
  for(int i = 0; i < m; i++){
    cin >> vests[i];
  }
  int i = 0;
  vector<pair<int,int>> res;
  for(int j = 0;  j< m; j++){
    		while (i < n && vests[j] > soldiers[i] + y) {		// The current vest is already bigger
			i++;
		}
    if(i == n) break;
    if(soldiers[i] - x <= vests[j] && vests[j] <= soldiers[i] + y){
      res.push_back({i+1, j+1});
       k++;i++;
    }
  }
  
  cout << k << endl;
  for(int i = 0; i < k; i++){
    int u = res[i].first;
    int v = res[i].second;
    cout << u << " " << v <<endl;
  }
  
  return 0;
}