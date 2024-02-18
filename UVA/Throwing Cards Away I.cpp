#include<bits/stdc++.h> 

using namespace std;

void solve(int n){
  if(n <= 0) return;
	queue<int> q;
  for(int i = 1; i <= n; i++){
    q.push(i);
  }
  vector<int> v;
  cout << "Discarded cards:";
  while(q.size() >= 2){
    int x = q.front();
    cout << " " << x;
    if(q.size()>2){
      cout << ",";
    }
    q.pop();
    int y = q.front();
    q.pop();
    q.push(y);
  }
  cout << endl;
  cout << "Remaining card: " << q.front() << endl;
  
}

int main(){
  int n;
  cin >> n;
	while(n!=0){
      solve(n);
    	cin >> n;
  }
  return 0;
}