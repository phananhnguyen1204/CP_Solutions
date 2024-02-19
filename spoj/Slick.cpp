#include <bits/stdc++.h>
#define MAX 251

using namespace std;

int N,M;
vector<vector<int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}};
vector<vector<int>> grid;
vector<vector<bool>> visited;
vector<int> cnt(MAX*MAX,0);

struct Cell{
  int r,c;
};


bool valid(int r, int c){
  return r >= 0 && r < N && c >= 0 && c < M && grid[r][c] == 1;
}

void bfs(Cell s){
  int size = 1;
  queue<Cell>q;
  visited[s.r][s.c] = true;
  q.push(s);
  while(!q.empty()){
    Cell u = q.front();
    q.pop();
    for(auto dir: dirs){
      int nr = u.r + dir[0];
      int nc = u.c + dir[1];
      if(valid(nr,nc) && !visited[nr][nc]){
        size++;
        q.push((Cell){nr,nc});
        visited[nr][nc] = true;
      }
    }
  }
  cnt[size]++;
}


int main(){
  while(true){
    cin >> N >> M;
    if(N == 0 && M ==0) break;
    grid = vector<vector<int>>(N,vector<int>(M));
    visited = vector<vector<bool>>(N, vector<bool>(M,false));
    fill(cnt.begin(),cnt.end(),0);
    for(int r = 0; r < N; r++){
      for(int c = 0; c < M; c++){
        cin >> grid[r][c];
      }
    }
    int n_slick = 0;
    for(int r = 0; r < N; r++){
      for(int c = 0; c < M; c++){
        if(!visited[r][c] && grid[r][c] == 1){
          bfs((Cell){r,c});
          n_slick++;
        }
      }
    }
    cout << n_slick << endl;
    for(int i = 1; i <= N*M; i++){
      if(cnt[i] != 0){
        cout << i << " " << cnt[i] << endl;
      }
    }
  }

  return 0;
}