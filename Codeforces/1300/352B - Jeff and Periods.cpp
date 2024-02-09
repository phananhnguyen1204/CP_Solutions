
#include <bits/stdc++.h>
#define MAX 1e9 + 5
using namespace std;


int n;


int main()
{
    cin >> n;
    vector<int> v(n);
    map<int,vector<int>> freqs;
    for(int i = 0; i < n; i++){
        cin >> v[i];
        freqs[v[i]].push_back(i);
    }
    int cnt = 0;
    vector<vector<int>> ans;
    for(auto [key,value]: freqs){
        if(value.size() == 1){
            ans.push_back({key,0});
            cnt++;
        }
        else if(value.size() == 2){
            ans.push_back({key,value[1]-value[0]});
            cnt++;
        }
        else{
            bool flag = false;
            int diff = value[1] - value[0];
            for(int i = 0; i < value.size() -1; i++){
                if(diff!= value[i+1] - value[i]){
                    flag = true;
                    break;
                }
            }
            if(!flag){
                ans.push_back({key,diff});
                cnt++;
            }
        }
    }
        cout << cnt << endl;
        for(auto x: ans){
            cout << x[0] << " " << x[1] << endl;
        }

    

    return 0;
}
