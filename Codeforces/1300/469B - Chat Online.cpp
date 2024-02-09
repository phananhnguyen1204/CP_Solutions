#include <bits/stdc++.h>

using namespace std;


int a,b,c,d;
int p,q,l,r;
int main()
{
    cin >> p >> q >> l >> r;
    vector<pair<int,int>> z(p);
    for(int i = 0; i < p; i++){
        cin >> a >> b;
        z[i] = {a,b};
    }
    vector<pair<int,int>> x(q);
    for(int i = 0; i < q; i++){
        cin >> c >> d;
        x[i] = {c,d};
    }
    
    int res = 0;
    for(int t = 0; t < r - l +1; t++){
        bool found = false;
        for(int i = 0; i < p; i++){
            for(int j = 0; j < q; j++){
                if(x[j].first + l + t >= z[i].first && x[j].first + l + t <= z[i].second){
                    found = true;
                }
                else if(x[j].second + l + t >= z[i].first && x[j].second + l + t <= z[i].second){
                    found = true;
                }
                else if(x[j].first + l + t <= z[i].first && x[j].second + l + t >= z[i].second){
                    found = true;
                }
                
                if(found){
                    break;
                }
            }
            if(found){
                break;
            }
        
        }
        if(found){
            res ++;
        }
    }
    cout << res;
    
    return 0;
}
