#include <bits/stdc++.h>

using namespace std;

int n,x;

int main(){
	while(true){
    cin >> n;
    stack<int> s;
    if(n == 0) break;
    vector<int> v(n);
    for(int i = 0 ;i < n; i++){
      cin >> v[i];
    }
    int curr = 1;
   	int i = 0;
    while(i < n){
      if(v[i] == curr){
        curr++;
        i++;
      }
      else if(!s.empty() && s.top() == curr){
        s.pop();
        curr++;
      }
      else{
        s.push(v[i]);
        i++;
      }
    }
    while(!s.empty() && s.top() == curr){
      s.pop();
      curr++;
    }
    cout << (curr == n+1 ? "yes": "no") << endl;
    
  }
  
  
  return 0;
}