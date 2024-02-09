#include <bits/stdc++.h>
#define INF 1e15
#define N 1e5 + 5

using namespace std;

typedef pair<int,int> ii;


int n,m,w,u,v;
vector<vector<ii>> graph(N);
vector<long long> dist(N,INF);
vector<int> path(N,-1);

void dijkstra(){
  priority_queue<ii, vector<ii>, greater<ii>> min_heap;
  dist[1] = 0;
  path[1] = 0;
  min_heap.push({dist[1],1});
  while(!min_heap.empty()){
    auto du = min_heap.top().first;
    auto u = min_heap.top().second;
    min_heap.pop();
    if(dist[u] != du) continue;
    
    for(auto [v,w] : graph[u]){
      if(dist[v] > dist[u] + w){
        dist[v] = dist[u] + w;
        path[v] = u;
        min_heap.push({dist[v], v});
        
      }
    }
  }
}


int main(){
  ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
  cin >> n >> m;
  for(int i = 0; i < m; i++){
    cin >> u >> v >> w;
    graph[u].push_back({v,w});
    graph[v].push_back({u,w});
  }
  dijkstra();
  if(dist[n] == INF){
    cout << -1;
    return 0;
  }
  int ptr = n;
  vector<int> temp;
  while(ptr != 0){
    temp.push_back(ptr);
    ptr = path[ptr];
  }
  reverse(temp.begin(), temp.end());
  for(auto i : temp){
    cout << i << " ";
  }
  
  
  
  return 0;
}