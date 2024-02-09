#include <bits/stdc++.h>

using namespace std;

int n,x;

int main()
{
    cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; i++){
        cin >> v[i];
    }
    int res = 0;
    int resource =0;
    while(true){
        for(int i = 0; i < n; i++){
            if(v[i] <= resource){
                v[i] = n+1;
                resource++;
            }
        }
        if(resource == n){
            break;
        }
        res++;
        for(int i = n-1; i >= 0; i--){
            if(v[i] <= resource){
                v[i] = n+1;
                resource++;
            }
        }
        if(resource == n){
            break;
        }
        res++;
    }
    cout << res;
    

    return 0;
}
