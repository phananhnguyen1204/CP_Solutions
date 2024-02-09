#include <bits/stdc++.h>

using namespace std;


int n;
int a,b;
int main()
{
    
    cin >> n;
    vector<int> x,y;
    for(int i = 0; i < n; i++){
        cin >> a >> b;
        x.push_back(a);
        y.push_back(b);
    }
    sort(x.begin(), x.end());
    sort(y.begin(), y.end());
    long long res = max(x[x.size()-1] - x[0], y[y.size()-1] - y[0]);
    cout << res * res;
    
    return 0;
}
