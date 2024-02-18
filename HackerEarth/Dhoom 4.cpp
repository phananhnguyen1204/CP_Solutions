#include <bits/stdc++.h>
#define MAX 100000+5
#define MOD 100000

using namespace std;

long long n,x,y,e;
vector<long long> dist;
vector<long long> key;

long long bfs(long long x, long long y){
  dist[x] = 0;
  queue<long long> q;
  q.push(x);
  while(!q.empty()){
    auto u = q.front();
    q.pop();
    if(u == y){
      return dist[y];
    }
    for(int i = 0; i < n; i++){
      auto nextValue = (1LL * u * key[i])%MOD;
      if(dist[nextValue] == -1){
        dist[nextValue] = dist[u] + 1;
        q.push(nextValue);
      }
    }
  }
  return -1;
}


int main(){
  cin >> x >> y;
  cin >> n;
  key = vector<long long >(n);
  dist = vector<long long>(MAX,-1);
  for(int i = 0; i < n; i++){
    cin >> key[i];
  }
  cout << bfs(x,y);

  return 0;
}

