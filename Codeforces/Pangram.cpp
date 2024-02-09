#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<bool> visited(26,false);
  int n;
  char c;
  cin >> n;
  for(int i = 0;i<n;i++){
    cin >> c;
    visited[tolower(c)-'a'] =true;
  }
  string res = "YES";
  for(int i = 0; i<26;i++){
    if(!visited[i]){
      res = "NO";
      break;
    }
  }
  cout << res << endl;
  
  
  return 0;
}