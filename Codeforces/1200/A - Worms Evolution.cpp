#include <bits/stdc++.h>

using namespace std;

int n;
string s;


int main()
{
    cin >> n;
    vector<int> v(n);
    unordered_map<int,int> s;
    for(int i = 0; i < n; i++){
        cin >> v[i];
        s[v[i]] = i;
    }
    for(int i = 0; i < n-1; i++){
        for(int j = i+1; j < n; j++){
                if(s.find(v[i] + v[j]) != s.end()){
                    cout << s[v[i] + v[j]] + 1 <<" "<< i + 1 << " " << j + 1;
                    return 0;
                }
        }
    }
    cout << -1;
    
    return 0;
}
