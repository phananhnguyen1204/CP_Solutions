#include <bits/stdc++.h>

using namespace std;

int k;
string s;

int main(){
  cin >> k >> s;
	int sum = 0;
	for(char c : s){
    sum += c - '0';
  }
  sort(s.begin(), s.end());
	int res = 0;
  int i = 0;
  while(sum <k){
    sum += '9' - s[i];
    res++;
    i++;
  }
  cout << res;
  
  return 0;
}