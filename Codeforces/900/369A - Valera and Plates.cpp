#include <bits/stdc++.h>

using namespace std;

int n,m,k;



int main()
{
    //bowls // plates
    cin >> n >> m >> k;
    vector<int> v(n);
    for(int i = 0; i < n; i++){
        cin >> v[i];
    }
    int cnt = 0;
    for(auto x: v){
        if(x == 1){
            if(m == 0){
                cnt++;
            }
            else{
                m--;
            }
        }
        else{
            if(k == 0 && m == 0){
                cnt++;
            }
            else{
                if(k==0){
                    m--;
                }
                else{
                    k--;
                }
            }
        }
    }
     cout << cnt;

    
    return 0;
}
