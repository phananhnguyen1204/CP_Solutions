#include <bits/stdc++.h>
#define MAX 105

using namespace std;

int n,m,u,v;
int parent[MAX], ranks[MAX];

void makeSet(){
  for(int i = 0; i < MAX; i++){
    parent[i] = i;
    ranks[i] = 0;
  }
}

int findSet(int u){
  if(u != parent[u]){
    parent[u] = findSet(parent[u]);
  }
  return parent[u];
}

void unionSet(int u, int v){
  int up = findSet(u);
  int vp = findSet(v);
  if(vp == up){
    return;
  }
  if(ranks[vp] < ranks[up]){
    parent[vp] = up;
  }
  else if(ranks[vp] > ranks[up]){
    parent[up] = vp;
  }
  else{
    parent[up] = vp;
    ranks[vp]++;
  }
}


int main(){
  cin >> n >> m;
  if(n != m){
    cout << "NO";
    return 0;
  }
  makeSet();
  for(int i = 0; i < m; i++){
    cin >> u >> v;
    unionSet(u,v);
  }
  
  int n_group = 0;
  for(int i = 1; i <= n; i++){
    if(i == parent[i]){
      n_group++;
    	if(n_group > 1){
      	break;
    	}
    }
  }
  cout << (n_group == 1 ? "FHTAGN!" : "NO");
  
  return 0;
}