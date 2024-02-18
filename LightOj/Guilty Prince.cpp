#include<bits/stdc++.h>
#define MAX 21

using namespace std;

struct Cell{
  int r, c;
};

int W,H,T;
vector<vector<char>> grid;
vector<vector<bool>> visited;
vector<vector<int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}};
Cell s;

int valid(int r, int c){
  return r >= 0 && r < H && c >= 0 && c < W && grid[r][c] == '.';
}

int bfs(Cell s){
  int res = 1;
  visited[s.r][s.c] = true;
  queue<Cell> q;
  q.push(s);
  while(!q.empty()){
  	Cell u = q.front();
    q.pop();
    for(auto dir: dirs){
      int nr = u.r + dir[0];
      int nc = u.c + dir[1];
      if(valid(nr,nc) && !visited[nr][nc]){
        q.push((Cell){nr,nc});
        visited[nr][nc] = true;
        res++;
      }
    }
  }
  return res;
}

int main(){
	cin >> T;
  for(int tc = 1; tc <= T; tc++){
    cout << "Case " << tc << ": ";
    cin >> W >> H;
    grid = vector<vector<char>>(H,vector<char>(W));
    visited = vector<vector<bool>>(H, vector<bool>(W,false));
    for(int r = 0; r < H; r++){
      for(int c = 0; c < W; c++){
        cin >> grid[r][c];
        if(grid[r][c] == '@'){
          s.r = r;
          s.c = c;
        }
      }
    }
    cout << bfs(s) << endl;
  }
  return 0;
}