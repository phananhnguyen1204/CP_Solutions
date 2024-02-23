#include <bits/stdc++.h>

using namespace std;

struct Cell{
  int r,c;
};

int t,R,C;
vector<vector<int>> dirs = {{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
vector<string> grid;
vector<vector<bool>> visited;
string target = "ALLIZZWELL";
bool found;

bool valid(int r, int c){
  return r >= 0 && r < R && c >=0 && c < C;
}

void dfs(Cell s, int index){
  visited[s.r][s.c] = true;
  if(index == target.length()-1){
    found = true;
    return;
  }
  for(auto dir: dirs){
    int nr = s.r + dir[0];
    int nc = s.c + dir[1];
    if(valid(nr,nc) && grid[nr][nc] == target[index+1] && !visited[nr][nc]){
      dfs((Cell){nr,nc},index+1);
    }
  }
  visited[s.r][s.c] = false;
}

int main(){
  cin >> t;
  while(t--){
    cin >> R >> C;
    grid = vector<string>(R);
    visited = vector<vector<bool>>(R,vector<bool>(C,false));
    for(int r = 0; r < R; r++){
      cin >> grid[r];
    }
   	found = false;
    for(int r = 0; r < R; r++){
      for(int c = 0; c < C; c++){
        if(grid[r][c] == 'A'){
          dfs((Cell){r,c}, 0);
        }
        if(found) break;
      }
      if(found) break;
    }
    cout << (found ? "YES" : "NO") << endl;
  }
  
  
  
  return 0;
}