#include <bits/stdc++.h>

const int MAX = 205;

using namespace std;

int k,n,m,u,v;
int parent[MAX], ranks[MAX];

void makeSet(){
  for(int i = 0; i < MAX; i++){
    parent[i] = i;
    ranks[i] = 0;
  }
}

int findSet(int u ){
  if(parent[u] != u){
    parent[u] = findSet(parent[u]);
  }
  return parent[u];
}

void unionSet(int v, int u){
  int vp = findSet(v);
  int up = findSet(u);
  if(vp == up){
    return;
  }
  if(ranks[vp] > ranks[up]){
    parent[up] = vp;
  }
  else if(ranks[vp] < ranks[up]){
    parent[vp] = up;
  }
  else{
    ranks[vp]++;
    parent[up] = vp;
  }
}

int main(){
  cin >> n >> m;
  int cnt_zero = 0;
  makeSet();
  for(int i = 1; i <= n; i++){
    cin >> k;
    if(k == 0){
      cnt_zero++;
    }
    else{
      for(int j = 0; j < k; j++){
        cin >> u;
        unionSet(i,u+n);
      }
    }
  }
  int res = -1;
  if(cnt_zero == n){
    res = n;
  }
  else{
    for(int i = 1; i <= n; i++){
      if(parent[i] == i){
        res++;
      }
    }
  }
  cout << res << endl;
  
  
  
  
  
  return 0;
}