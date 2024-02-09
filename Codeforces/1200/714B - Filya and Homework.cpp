#include <bits/stdc++.h>

using namespace std;

unordered_set<int> s;
int n,x;


int main()
{
    cin >> n;
    vector<int> v;
    for(int i = 0; i < n; i++){
        cin >> x;
        s.insert(x);
    }
    if(s.size() == 1){
        cout << "YES";
    }
    else if(s.size() > 3){
        cout << "NO";
    }
    else if(s.size() == 2){
        cout << "YES";
    }
    else{
        for(auto x: s){
            v.push_back(x);
        }
        sort(v.begin(),v.end());
        cout << ((v[2] + v[0] == 2* v[1]) ? "YES" : "NO");
    }
    return 0;
}
