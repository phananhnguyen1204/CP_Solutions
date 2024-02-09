#include <bits/stdc++.h>

using namespace std;


string s;

int main()
{
    vector<pair<int,char>> v(4);
    for(int i = 0; i < 4; i++){
        cin >> s;
        v[i] = {s.length()-2, s[0]};
    }
    sort(v.begin(),v.end());
    vector<char> ans;
    if(2 *v[0].first <= v[1].first){
        ans.push_back(v[0].second);
    }
    if(2 * v[2].first <= v[3].first){
        ans.push_back(v[3].second);
    }
    if(ans.size() == 1){
        cout << ans[0];
    }
    else{
        cout << "C";
    }

    
    return 0;
}
