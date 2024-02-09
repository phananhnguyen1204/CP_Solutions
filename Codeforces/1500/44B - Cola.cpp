#include <bits/stdc++.h>

double n,a,b,c;

using namespace std;

int main(){
  cin >> n >> a >> b >> c;
  int cnt = 0;
  for(int i = 0; i <= a; i++){
    for(int j = 0; j <= b; j++){
      double sum = i*0.5 + j;
      if(sum > n){
        continue;
      }
      sum = (n-sum)/2;
 			if((sum - ceil(sum)) == 0 && 0 <= sum && sum <= c){
        cnt++;
      }
    }
  }
  cout << cnt;
  
  
  
  return 0;
}