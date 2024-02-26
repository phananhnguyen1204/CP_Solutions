#include <bits/stdc++.h>
#define MAX 51

using namespace std;

int H,W,tc,cnt,res;
vector<string> grid;
vector<vector<int>> dirs = {{1,0},{-1,0},{-1,-1},{1,-1},{0,1},{0,-1},{1,1},{-1,1}};

bool valid(int r, int c){
  return (r >=0 && r < H && c >=0 && c < W);
}

void dfs(int r, int c, int len){
	res = max(len,res);
  for(auto dir: dirs){
    int nr = r + dir[0];
    int nc = c + dir[1];
    if(valid(nr,nc) && (int)(grid[nr][nc] - grid[r][c]) == 1){
      dfs(nr,nc,len+1);
    }
  }
}

int main(){
  tc = 1;
  while(true){
    res = 0;
    cin >> H >> W;
    if(H == 0 && W == 0) break;
    grid = vector<string>(H);
    for(int r = 0; r < H; r++){
      cin >> grid[r];
    }
    for(int r = 0; r < H; r++){
      for(int c = 0; c < W; c++){
        if(grid[r][c] == 'A'){
          dfs(r,c,1);
        }
      }
    }
    cout << "Case " << tc << ": " << res << endl;
    tc++;
  }
  return 0;
}