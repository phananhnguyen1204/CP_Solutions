
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

int n,m;


int main()
{
    cin >> n >> m;
    vector<int> prices(n);
    for(int i = 0; i < n; i++){
        cin >> prices[i];
    }
    sort(prices.begin(), prices.end());
    int cnt = 0;
    for(int i =0 ; i < m; i++){
        if(prices[i] >= 0){
            cout << cnt;
            return 0;
        }
        cnt -= prices[i];
    }
    cout << cnt;

    return 0;
}
