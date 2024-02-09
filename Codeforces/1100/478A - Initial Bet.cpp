

#include <bits/stdc++.h>

using namespace std;

int c;

int main()
{
    int cnt = 0;
    for(int i = 0; i < 5; i++){
        cin >> c;
        cnt += c;
    }
    if(cnt == 0){
        cout << -1;
        return 0;
    }
    cout << (cnt % 5 == 0 ? cnt/5 : -1);
    return 0;
}
