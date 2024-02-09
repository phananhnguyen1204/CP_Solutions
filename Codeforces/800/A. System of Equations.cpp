
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

int n,m;


int main()
{
    cin >> n >> m;
    int cnt = 0;
    for(int i = 0 ; i <= sqrt(n); i++){
        for(int j = 0; j <= sqrt(m); j++){
            if((i*i + j == n) && (j*j + i == m)){
                cnt++;
            }
        }
    }
    cout << cnt;

    return 0;
}
