#include <bits/stdc++.h>

using namespace std;
int P,C,x,temp;
char command;

int main(){
  int tc = 0;
  while(true){
    cin >> P >> C;
    if(P == 0 && C == 0){
      break;
    }
    queue<int> q;
    tc++;
    cout << "Case " << tc << ":" << endl;
    for(int i = 1;i <= min(P,C); i++){
      q.push(i);
    }
    
    for(int i = 0; i < C; i++){
      cin >> command;
      if(command == 'N'){
        cout << q.front() << endl;
        temp = q.front();
        q.pop();
        q.push(temp);
      }
      else{
        cin >> x;
        int n = q.size();
        q.push(x);
        for(int j = 0; j < n; j++){
          temp = q.front();
          q.pop();
          if(temp != x){
            q.push(temp);
          }
        }
      }
    }
  }
  
  return 0;
}