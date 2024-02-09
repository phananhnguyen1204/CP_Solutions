
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

int n,a,b;


int main()
{
    cin >> n >> a >> b;

    cout << ( n - max(a+1 , n-b) + 1);

    return 0;
}
