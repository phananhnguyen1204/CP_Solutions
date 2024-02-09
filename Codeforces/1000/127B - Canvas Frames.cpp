#include <bits/stdc++.h>

using namespace std;

int n,x;

int main()
{
    
    cin >> n;
    vector<int> v(105,0);
    for(int i = 0; i < n; i++){
        cin >> x;
        v[x]++;
    }
    int total = 0;
    for(int i = 1; i <= 100; i++){
        total += v[i] /2;
    }
    cout << total/2;
    return 0;
}
