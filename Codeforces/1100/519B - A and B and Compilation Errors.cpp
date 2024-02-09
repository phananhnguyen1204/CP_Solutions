#include <bits/stdc++.h>

using namespace std;

int n,x;

int main()
{
    cin >> n;
    long long sum = 0;
    for(int i = 0; i < n; i++){
        cin >> x;
        sum += x;
    }
    long long sum1 = 0;
    for(int i = 0; i < n -1 ; i++ ){
        cin >> x;
        sum1 += x;
    }
    cout << sum - sum1 << endl;
    sum = 0;
    for(int i = 0; i < n-2; i++){
        cin >> x;
        sum += x;
    }
    cout << sum1 - sum;

    return 0;
}
