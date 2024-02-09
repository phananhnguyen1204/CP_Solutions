#include <bits/stdc++.h>
#define MAX 105

using namespace std;

int parent[MAX], ranks[MAX];
int n,x,y;

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
 	if(ranks[vp] > ranks[up]){
    parent[up] = vp;
  }
  else if(ranks[vp] < ranks[up]){
    parent[vp] = up;
  }
  else{
    parent[up] = vp;
    ranks[vp]++;
  }
}


bool isSameSet(pair<int,int> a, pair<int,int> b){
  return( a.first == b.first || a.second == b.second);
}

int main(){
  cin >> n;
  vector<pair<int,int>> p(n);
  makeSet();
  for(int i = 0; i < n; i++){
    cin >> x >> y;
		p[i].first = x;
    p[i].second = y;
    for(int j = 0; j < i; j++){
      if(isSameSet(p[j],p[i])){
        unionSet(i,j);
      }
    }
  }
  
  int n_group = 0;
  for(int i = 0; i < n; i++){
    if(parent[i] == i){
      n_group++;
    }
  }
  cout << (n_group - 1) << endl;
  
  return 0;
}