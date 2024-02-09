#include <bits/stdc++.h>
#define ll long long

using namespace std;

ll n,b,t,d;
ll processing;

int main(){
  cin >> n >> b;
  queue<ll> q;
  for(auto i = 0; i < n; i++){
    cin >> t >> d;
    while(!q.empty() && q.front() <=t){
      q.pop();
    }
    if(q.size() <= b){
      processing = max(processing, t) + d;
      cout << processing << " ";
      q.push(processing);
    }
    else{
      cout << -1 << " ";
    }
  }
  
  
  return 0;
}