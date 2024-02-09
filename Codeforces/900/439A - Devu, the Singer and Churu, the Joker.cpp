#include <bits/stdc++.h>

using namespace std;

int n,d,t;

int main()
{
    cin >> n >> d;
    int sum = 0;
    for(int i = 0; i < n; i++){
        cin >> t;
        sum += t;
    }
    if(sum + (n-1) * 10 > d){
        cout << -1;
    }
    else{
        cout << (d - sum) /5;
    }
    
    

    return 0;
}
