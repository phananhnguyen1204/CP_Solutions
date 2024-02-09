#include <bits/stdc++.h>

const int MAX = 2000 + 5;


using namespace std;

int n,h;
pair<int,int> p[MAX];


int main(){
  cin >> n;
  for(int i = 0; i < n; i++){
    cin >> p[i].first;
    p[i].second = i;
  }
  sort(p, p + n);
  int pairs = 0;
  for(int i = 0; i < n - 1; i++){
    if(p[i].first == p[i+1].first){
      pairs++;
    }
    if(pairs == 2){
      cout << "YES" << endl;
      for(int j = 0; j < n; j++){
        cout << (p[j].second + 1) << " ";
      }
      cout << endl;
      pairs = 0;
      for(int j = 0; j < n - 1; j++){
        if(p[j].first == p[j+1].first){
          pairs++;
          swap(p[j].second, p[j+1].second);
          for(int k = 0; k < n; k++){
						cout << (p[k].second + 1) << " ";         
          }
          cout << endl;   
          swap(p[j].second, p[j+1].second);
        }
        if(pairs == 2){
          return 0;
        }
      }
    }
  }
  cout << "NO" << endl;
  
  return 0;
}