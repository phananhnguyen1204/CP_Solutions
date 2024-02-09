#include <bits/stdc++.h>
#define MAX 51

using namespace std;

struct Cell{
  int r, c;
};

int n,m,k;
bool isOcean;
bool visited[MAX][MAX];
string lake[MAX];
vector<int> dir[] ={{1,0}, {-1,0}, {0,-1}, {0,1}};
vector<vector<Cell>> lakes;
vector<Cell> temp;

bool valid(int r, int c){
  return (r >= 0 && r < n && c >= 0 && c < m);
}

bool onBorder(int r, int c){
  return (r == 0 || c==0 || r == n-1 || c == m-1);
}

bool sort_by_size(vector<Cell> a, vector<Cell> b){
  return a.size() < b.size();
}

void dfs(Cell s){
  visited[s.r][s.c] = true;
  temp.push_back(s);

  for(int i = 0; i < 4; i++){
    int r = s.r + dir[i][0];
    int c = s.c + dir[i][1];
    if(onBorder(s.r,s.c)){
   		isOcean = true;
  	}
    if(valid(r,c) && !visited[r][c] && lake[r][c] == '.'){
      dfs((Cell) {r,c});
    }
  }
  
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n >> m >> k;

  for(int i = 0; i < n; i++){
    cin >> lake[i];
  }
  
  for(int r = 0; r < n; r++){
    for(int c = 0; c < m; c++){
      if(lake[r][c] == '.' && !visited[r][c]){
        isOcean = false;
        temp.clear();
				dfs((Cell){r,c});
        if(!isOcean){
          lakes.push_back(temp);
        }
      }
    }
  }
  
  sort(lakes.begin(),lakes.end(),sort_by_size);
  int res = 0;
  for(auto i = 0; i < (lakes.size() - k); i++){
    res += lakes[i].size();
    for(auto j = 0; j < lakes[i].size(); j++){
      Cell x = lakes[i][j];
      lake[x.r][x.c] = '*';
    }
  }
  
  cout << res << endl;
  for(auto i = 0; i < n; i++){
    cout << lake[i] << endl;
  }

  
  return 0;
}