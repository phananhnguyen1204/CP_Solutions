#include <bits/stdc++.h>

using namespace std;

int n,m;

unordered_map<string, string> dic;
string s1,s2,s;

int main()
{
    cin >> n >> m;
    for(int i = 0; i < m; i++){
        cin >> s1 >> s2;
        if(s1.length() <= s2.length()){
            dic[s1] = s1;
            dic[s2] = s1;
        }
        else{
            dic[s1] = s2;
            dic[s2] = s2;
        }
    }
    for(int i = 0; i < n; i++){
        cin >> s;
        cout << dic[s] << " ";
    }

    return 0;
}
