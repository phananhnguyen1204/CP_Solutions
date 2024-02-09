#include <bits/stdc++.h>

using namespace std;

int n;

int main()
{
    cin >> n;
    int curr_h = 0;
    vector<int> v(n);
    for(int i = 0; i < n; i++){
        cin >> v[i];
    }
    int res = 0;
    curr_h = 0;
    for(int i = 0; i < n; i++){
        res += v[i] - curr_h + 1;
        curr_h = v[i];
        if(i != n-1){
            int x = min(v[i],v[i+1]);
            res += curr_h - x;
            curr_h = x;
            res++;
        }
    }
    cout << res;

    return 0;
}
