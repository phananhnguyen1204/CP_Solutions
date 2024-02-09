#include <bits/stdc++.h>

using namespace std;

int n,c,curr,last;
int main()
{
    cin >> n >> c;
    int cnt = 0;
    for(int i = 0; i < n; i++){
        cin >> curr;
        if(i == 0){
            cnt++;
        }
        else{
            if(curr - last > c){
                cnt = 1;
            }
            else{
                cnt++;
            }
        }
        last = curr;
    }
    cout << cnt;
    return 0;
}
