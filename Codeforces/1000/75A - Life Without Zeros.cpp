#include <bits/stdc++.h>

using namespace std;

int a,b;

int remove_zero(int n){
    int res = 0;
    int cnt = 1;
    while(n>0){
        if(n%10 != 0){
            res = cnt *( n%10) + res;
            cnt *= 10;           
        }
        n /= 10;
    }
    return res;
}

int main()
{
    cin >> a >> b;
    int c = a + b;
    int x =remove_zero(a);
    int y = remove_zero(b);
    cout << (x + y == remove_zero(c) ? "YES" : "NO");
    
    return 0;
}
