#include <bits/stdc++.h>
#define MAX 1000+5

using namespace std;

int n,q,s,u,v,m;

vector<vector<int>> graph;
vector<int> dist;

void bfs(int s){
  dist[s] = 0;
  queue<int> q;
  q.push(s);
  while(!q.empty()){
    int u = q.front();
    q.pop();
    for(auto v : graph[u]){
      if(dist[v] == -1){
        dist[v] = dist[u] + 6;
        q.push(v);
      }
    }
  }
}

int main(){
  cin >> q;
  while(q--){
    cin >> n >> m;
    graph = vector<vector<int>>(MAX,vector<int>());
    dist  = vector<int>(MAX,-1);
    for(int i = 0; i < m; i++){
      cin >> u >> v;
      graph[u].push_back(v);
      graph[v].push_back(u);
    }
    cin >> s;
    bfs(s);
    for(int i = 1; i <= n; i++){
      if(i == s) continue;
      cout << (dist[i]) << " ";
    }
    cout << endl;
  }
	
  
  
  return 0;
}
