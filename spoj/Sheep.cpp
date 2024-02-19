#include <bits/stdc++.h>
#define MAX 251

using namespace std;

struct Cell{
  int r,c;
};

int N,M;
int n_sheeps = 0,n_wolves = 0;
string grid[MAX];
vector<vector<int>> dirs = {{1,0},{-1,0},{0,-1},{0,1}};


bool valid(int r,int c){
  return (r>=0 && r<N && c>=0 && c<M);
}

void bfs(Cell s){
  queue<Cell> q;
  q.push(s);
  int sheeps = grid[s.r][s.c] == 'k', wolves = grid[s.r][s.c] == 'v';
  grid[s.r][s.c] = '#';
  bool escape = false;
  while(!q.empty()){
    Cell u = q.front();
    q.pop();
    for(auto dir: dirs){
      int nr = u.r + dir[0];
      int nc = u.c + dir[1];
      if(!valid(nr,nc)) escape = true;
      if(valid(nr,nc) && grid[nr][nc] != '#'){
        if(grid[nr][nc] == 'k') sheeps++;
        if(grid[nr][nc] == 'v') wolves++;
        grid[nr][nc] = '#';
        q.push((Cell){nr,nc});
      }
    }
  }
  if(escape){
    n_sheeps += sheeps;
    n_wolves += wolves;
  }
  else{
    if(sheeps > wolves){
      n_sheeps += sheeps;
    }
    else n_wolves += wolves;
  }
}



int main(){
  cin >> N >> M;
  for(int r = 0; r < N; r++){
		cin >> grid[r];
  }
  for(int r = 0; r < N; r++){
    for(int c = 0; c < M; c++){
      if(grid[r][c] != '#'){
        bfs((Cell){r,c});
      }
    }
  }
  cout << n_sheeps << " " << n_wolves;
  
  return 0;
}

