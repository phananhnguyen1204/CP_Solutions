

#include <bits/stdc++.h>

using namespace std;

int n;
string s;
unordered_set<string> seen;

int main()
{
    seen.insert("ABSINTH");
    seen.insert("BEER");
    seen.insert("BRANDY");
    seen.insert("CHAMPAGNE");
    seen.insert("GIN");
    seen.insert("RUM");
    seen.insert("SAKE");
    seen.insert("TEQUILA");
    seen.insert("VODKA");
    seen.insert("WHISKEY");
    seen.insert("WINE");
    cin >> n;
    int res = 0;
    for(int i = 0; i < n; i++){
        cin >> s;
        if(isdigit(s[0])){
            if(stoi(s) < 18){
                res++;
            }
        }
        else{
            if(seen.find(s) != seen.end()){
                res++;
            }
        }
    }
    cout << res;
    

    return 0;
}
