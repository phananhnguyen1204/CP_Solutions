#include <bits/stdc++.h>
#define MAX 100000 + 5

using namespace std;

int t,N,e,a,b;

vector<vector<int>> graph;
vector<bool> visited;

void dfs(int u){
  visited[u] = true;
  for(auto v: graph[u]){
    if(!visited[v]){
      dfs(v);
    }
  }
}

int main(){
  cin >> t;
  while(t--){
    cin >> N >> e;
    graph = vector<vector<int>>(MAX,vector<int>());
    visited = vector<bool>(MAX,false);
    for(int i = 0; i < e; i++){
      cin >> a >> b;
      graph[a].push_back(b);
      graph[b].push_back(a);
    }
    int cnt = 0;
    for(int i = 0; i < N; i++){
      if(!visited[i]){
        cnt++;
        dfs(i);
      }
    }
    cout << cnt << endl;
  }
  
  
  return 0;
}