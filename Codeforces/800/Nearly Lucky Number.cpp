#include <bits/stdc++.h>
#define ll long long
#define MAX 1e9

using namespace std;


ll n;

bool check(ll x){
    while(x > 0){
        int digit = x % 10;
        if(digit != 4 && digit != 7){
            return false;
        }
        x /= 10;
    }
    return true;
}

int main(){
    cin >> n;
    ll cnt = 0;
    while(n > 0){
        ll digit = n % 10;
        if(digit == 7 || digit == 4){
            cnt++;
        }
        n/=10;
    }
    if(cnt == 0){
        cout << "NO" << endl;
    }
    else{
        cout << (check(cnt) ? "YES" : "NO") << endl;
    }

  return 0;
}