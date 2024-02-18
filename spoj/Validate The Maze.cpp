#include <bits/stdc++.h>
#define MAX 21

using namespace std;

struct Cell{
  int r,c;
};

int t,m,n;
vector<vector<char>> matrix;
vector<vector<bool>> visited;
vector<vector<int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}};

bool isvalid(int r, int c){
  return r >= 0 && r < m && c >= 0 && c < n && matrix[r][c] == '.';
}

bool bfs(Cell s, Cell e){
  visited[s.r][s.c] = true;
  queue<Cell> q;
  q.push(s);
  while(!q.empty()){
    auto u = q.front();
    q.pop();
    if(u.r == e.r && u.c == e.c) return true;
    for(auto dir: dirs){
      auto nr = u.r + dir[0];
      auto nc = u.c + dir[1];
      if(isvalid(nr,nc) && !visited[nr][nc]){
        q.push((Cell){nr,nc});
        visited[nr][nc] = true;
      }
    }
  }
  return false;
} 


int main(){
	cin >> t;
  while(t--){
    cin >> m >> n;
    matrix = vector<vector<char>>(m,vector<char>(n));
    visited = vector<vector<bool>>(m,vector<bool>(n,false));
    vector<Cell> entrances;
    for(int r = 0;r < m; r++){
      for(int c = 0; c < n; c++){
        cin >> matrix[r][c];
       	if(r == 0 || c == 0 || r == m-1 || c == n-1){
          if(matrix[r][c] == '.'){
            entrances.push_back((Cell){r,c});
          }
        }
      }
    }
    if(entrances.size() != 2){
      cout << "invalid" << endl;
      continue;
    }
    Cell s = entrances[0];
    Cell e = entrances[1];
    cout << (bfs(s,e) ? "valid" : "invalid") << endl;
    
  }
  
  return 0;
}