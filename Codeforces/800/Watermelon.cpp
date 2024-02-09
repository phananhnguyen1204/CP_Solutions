#include <bits/stdc++.h>
#define ll long long

using namespace std;

int weight;

int main(){
    cin >> weight;
    bool found = false;
    for(int i = 2; i < weight; i+=2){
        if((weight - 2) % 2 == 0){
            found = true;
            break;
        }
    }
    cout << (found ? "YES" : "NO") << endl;

  
  return 0;
}