#include <bits/stdc++.h>
#define MAX 1000+5

using namespace std;

vector<bool> visited;
int N,Q;
vector<vector<int>> graph;
vector<int> dist;

void dfs(int u, int distance){
  dist[u] = distance;
  visited[u] = true;
  for(auto v: graph[u]){
    if(!visited[v]){
      dfs(v,distance+1);
    }
  }
}

int main(){
  int u, v, x, res;
  cin >> N;
  visited = vector<bool>(MAX, false);
  graph = vector<vector<int>>(MAX, vector<int>());
  dist = vector<int>(MAX,0);
  for(int i = 0; i < N-1 ; i++){
    cin >> u >> v;
    graph[u].push_back(v);
    graph[v].push_back(u);
  }
  dfs(1,0);
  cin >> Q;
  int curr_dist = 1e9;
  for(int i = 0; i < Q; i++){
    cin >> x;
    if(curr_dist > dist[x]){
      curr_dist = dist[x];
      res = x;
    }
    else if(curr_dist == dist[x]){
      res = min(res,x);
    }
  }
  cout << res;
  
  return 0;
}