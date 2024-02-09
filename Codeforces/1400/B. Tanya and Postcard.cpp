#include <bits/stdc++.h>

using namespace std;

string s,t;
unordered_map<int,int> freqs1;
unordered_map<int,int> freqs2;

int main(){
  cin >> s >> t;
  for(char c:s){
    int index = c - 'A';
    if(c > 'Z'){
      index = c - 'a' + 26;
    }
    freqs1[index]++;
  }
  
  for(char c: t){
    int index = c - 'A';
    if(c > 'Z'){
      index = c - 'a' + 26;
    }
    freqs2[index]++;    
  }
  
  int res1 = 0;
  int res2 = 0;
  for(int i = 0; i < 26; i++){
    int temp1 = min(freqs1[i],freqs2[i]);
    int temp2 = min(freqs1[i+26],freqs2[i+26]);
    res1 += temp1 + temp2;
    freqs1[i] -= temp1;
    freqs2[i] -= temp1;
    freqs1[i+26] -= temp2;
    freqs2[i+26] -= temp2;
  }
  
  for(int i =0; i < 26; i++){
    int temp = min(freqs1[i], freqs2[i+26]) + min(freqs1[i+26], freqs2[i]);
    res2 += temp;
  }
  
  cout << res1 << " " << res2 << endl;
  
  
  return 0;
}