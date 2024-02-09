#include <bits/stdc++.h>
#define MAX 501

using namespace std;

struct Cell{
  int r,c;
};

int n,m;
int r1,c1,r2,c2;
string level[MAX];
vector<int> dir[] = {{1,0}, {-1,0}, {0,-1}, {0,1}};

bool valid(int r, int c){
  return (r >= 0 && r < n && c >= 0 && c < m);
}

bool bfs(Cell s, Cell f){
  queue<Cell> q;
  q.push(s);
  level[s.r][s.c] = 'X';
  while(!q.empty()){
    auto u = q.front();
    q.pop();
    for(int i = 0; i < 4; i++){
      int r = u.r + dir[i][0];
      int c = u.c + dir[i][1];
      if(r == f.r && c == f.c && level[r][c] == 'X') return true;
      if(valid(r,c) && level[r][c] == '.'){
        q.push((Cell){r,c});
        level[r][c] = 'X';
      }
    }
  }
  return false;
}

int main(){
  Cell s, f;
  cin >> n >> m;
  for(int r = 0; r < n; r++){
    cin >> level[r];
  }
  cin >> s.r >> s.c >> f.r >> f.c;
  s.r -= 1;
  s.c -= 1;
  f.r -= 1;
  f.c -= 1;
  cout << (bfs(s,f) ? "YES" : "NO") << endl;
  return 0;
}