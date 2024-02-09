#include <bits/stdc++.h>

using namespace std;

string s;

int main()
{
    cin >> s;
    int res = 0;
    char prev;
    int i = 0;
    while(i < s.length()){
        int cnt = 0;
        prev = s[i];
        while(i < s.length() && prev == s[i] && cnt < 5){
            cnt++;
            i++;
        }
        res++;
    }
    cout << res;
    
    return 0;
}
