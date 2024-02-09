#include <bits/stdc++.h>

using namespace std;

int n;


int main()
{
    cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; i++){
        cin >> v[i];
    }
    int res = 1;
    for(int i = 0; i < n; i++){
        int cnt = 1;
        int l = i - 1;
        int r = i+1;
        for(int j = l; j >=0; j--){
            if(v[j] > v[j+1]){
                break;
            }
            else{
                cnt++;
            }
        }
        
        for(int j = r; j < n; j++){
            if(v[j] > v[j-1]){
                break;
            }
            else{
                cnt++;
            }
        }
        res = max(res, cnt);
    }
    cout << res;
    
    return 0;
}
