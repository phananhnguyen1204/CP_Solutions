#include <bits/stdc++.h>

using namespace std;

int n,m;

int main()
{
    cin >> n >> m;
    if(n == 0 && m == 0){
        cout << 0 << " " << 0;
        return 0;
    }
    if(n == 0){
        cout << "Impossible";
        return 0;
    }
    if(m == 0){
        cout << n << " " << n;
        return 0;
    }
    int max_res = (n-1) + m;
    int min_res = n + max(m-n,0);
    cout << min_res << " " << max_res;

    return 0;
}
