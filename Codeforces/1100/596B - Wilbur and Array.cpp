

#include <bits/stdc++.h>

using namespace std;

int n;

int main()
{
    cin >> n;
    vector<long long> v(n);
    long long res = 0;
    for(int i = 0; i < n; i++){
        cin >> v[i];
        if(i == 0){
            res += abs(v[i]);
        }
        else{
            res += abs(v[i] - v[i-1]);
        }
    }
    cout << res;

    return 0;
}
