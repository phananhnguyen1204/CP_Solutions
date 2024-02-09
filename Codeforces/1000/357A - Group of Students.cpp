#include <bits/stdc++.h>

using namespace std;

int n,a,b;
int main()
{
    cin >> n;
    vector<int> v(n);
    int total = 0;
    for(int i = 0; i < n; i++){
        cin >> v[i];
        total += v[i];
    }
    cin >> a >> b;
    
    for(int k = 1; k <= n; k++){
        int cnt = 0;
        for(int i = 0; i < k-1; i++){
            cnt += v[i];
        }
        if((a <= cnt && cnt <= b) && (a <= (total- cnt) && (total - cnt) <= b)){
            cout << k;
            return 0;
        }
    }
    cout << 0;
    return 0;
}
