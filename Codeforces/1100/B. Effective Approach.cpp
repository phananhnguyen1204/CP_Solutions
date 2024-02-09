
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

int n,x,m,target;
int v[MAX];

int main()
{
    cin >> n;
    memset(v,0,sizeof(v));
    for(int i = 1; i <= n; i++){
        cin >> x;
        v[x] = i;
    }
    cin >> m;
    long long Vasya =0 ;
    long long Petya = 0;
    for(int i = 0; i < m; i++){
        cin >> target;
        Vasya += v[target];
        Petya += (n - v[target] + 1);
        
    }
     cout << Vasya << " " << Petya << endl;
 

    return 0;
}
