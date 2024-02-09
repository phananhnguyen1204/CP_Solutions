#include <bits/stdc++.h>

using namespace std;

int a,b,s;

int main()
{
    cin >> a >> b >> s;
    if(abs(a) + abs(b) > s || (s - abs(a) - abs(b)) %2 == 1){
        cout << "NO";
    }
    else{
        cout << "YES";
    }
    
    return 0;
}
