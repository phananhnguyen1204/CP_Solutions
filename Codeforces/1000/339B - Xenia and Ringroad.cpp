#include <bits/stdc++.h>

using namespace std;

int n, m;

int main()
{
    
    cin >> n >> m;
    int prev = 1;
    long long res = 0;
    vector<int> v(m);
    for(int i = 0; i < m; i++){
        cin >> v[i];
    }
    
    for(int i = 0; i < m; i++){
        if(prev <= v[i]){
            res += v[i] - prev;
        }
        else{
            res += n - prev + v[i];
        }
        prev = v[i];
    }
    cout << res;
    

    return 0;
}
