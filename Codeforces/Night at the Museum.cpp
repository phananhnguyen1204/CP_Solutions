#include <iostream>
#include <string>

using namespace std;

int main(){
  string wheel;
  cin >> wheel;
  char pointer = 'a';
  int cnt = 0;
  for(char c: wheel){
    int diff = abs(c-pointer);
    if(diff >13){
      cnt += 26-diff;
    }
    else
      cnt += diff;
    pointer = c;
  }
  cout << cnt;
  return 0;
}