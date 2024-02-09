
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

long long n,k;

int main()
{
    cin >> n >> k;
    long long cnt_odd =0;
    long long cnt_even = 0;
    if(n%2==0){
        cnt_even = (n-2)/ 2 + 1;
        cnt_odd = cnt_even;
    }
    else{
        cnt_odd = (n-1)/2 + 1;
        cnt_even = cnt_odd - 1;
    }
    long long res;
    if(k <= cnt_odd){
        res = 1 + (k - 1)* 2;
    }
    else{
        res = 2 + (k- cnt_odd - 1)*2;
    }
    cout << res;
    

    return 0;
}
