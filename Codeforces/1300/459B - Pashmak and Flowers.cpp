
#include <bits/stdc++.h>
#define MAX 1e9 + 5
using namespace std;


long long n;


int main()
{
    cin >> n;
    vector<long long>v(n);
    unordered_map<long long,long long> cnt;
    for(int i = 0; i < n; i++){
        cin >> v[i];
        cnt[v[i]]++;
    }
    sort(v.begin(), v.end());
    if(v[n-1] == v[0]){
        cout << "0" << " " << (cnt[v[0]] * (cnt[v[0]] - 1)/2);
        return 0;
    }
    cout << (v[n-1] - v[0]) << " " << (cnt[v[n-1]] * cnt[v[0]]);
    

    return 0;
}
