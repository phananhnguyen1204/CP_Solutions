#include <bits/stdc++.h>
#define ll long long
#define MAX 1e9

using namespace std;


int y;

bool check(int num){
    vector<int> freqs(26,0);
    while(num > 0){
        int digit = num%10;
        if(freqs[digit] != 0){
            return false;
        }
        else{
            freqs[digit]++;
        }
        num/= 10;
    }
    return true;
}

int main(){
    cin >> y;
    for(int i = y+1; i <= MAX; i++){
        if(check(i)){
            cout << i;
            break;
        }
    }

  return 0;
}