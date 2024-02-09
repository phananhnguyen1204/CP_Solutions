#include <bits/stdc++.h>

using namespace std;

long long n,x;

int main()
{
    cin >> n;
    long long temp = n;
    long long cnt = 0;
    while(temp > 0){
        cnt++;
        temp /= 10;
    }
    long long res = cnt * (n+1) - 1;
    temp = 1;
    for(int i = 0; i < cnt - 1; i++){
        temp *= 10;
        res -= temp;
    }
    cout << res;
    
    return 0;
}
