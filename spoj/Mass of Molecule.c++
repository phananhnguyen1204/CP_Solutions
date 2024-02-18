#include <bits/stdc++.h>

using namespace std;

unordered_map<char,int> val;


int main(){
  val['C'] = 12;
	val['H'] = 1;
	val['O'] = 16;
  string molecule;
  cin >> molecule;
  int res = 0;
  stack<int> s;
  for(char c : molecule){
    if(isalpha(c)){
      s.push(val[c]);
    }
    else if(isdigit(c)){
      int top = s.top();
      s.pop();
      s.push(top*(c-'0'));
    }
    else if(c == '('){
      s.push(-1);
    }
    else{
      int sum = 0;
      while(s.top() != -1){
        sum += s.top();
        s.pop();
      }
      s.pop();
      s.push(sum);
    }
  }
  while(!s.empty()){
    res += s.top();
    s.pop();
  }
  cout << res;
	
  
  
  
  return 0;
}