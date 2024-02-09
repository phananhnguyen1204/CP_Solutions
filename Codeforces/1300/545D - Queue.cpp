#include <bits/stdc++.h>

using namespace std;

int n;

int main()
{
    
    cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; i++){
        cin >> v[i];
    }
    sort(v.begin(), v.end());
    long long prev = 0;
    int cnt = 0;
    for(int i = 0; i < n; i++){
        if(prev > v[i]){
            cnt++;
        }
        else{
            prev += v[i];
        }
    }
    cout << (n - cnt);
    return 0;
}
