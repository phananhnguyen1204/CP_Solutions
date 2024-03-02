#include <bits/stdc++.h>

using namespace std;

int T,S,p,N;
int score;

int main(){
  cin >> T;
  for(int tc = 1; tc <=T; tc++){
    int res = 0;
    cout << "Case #" << tc <<": ";
    cin >> N >> S >> p;
    for(int i = 0; i < N; i++){
      cin >> score;
      if(score == 0 && p != 0){
        continue;
      }
      if(score >= (3*(p-1)+1)){
        res++;
      }
      else if(S > 0 && score >= (3*(p-1)-1)){
        res++;
        S--;
      }
    }
    cout << res << endl;
  }
  
  return 0;
}