
#include <bits/stdc++.h>

using namespace std;

string s;
unordered_set<char> freqs;

int main()
{
    cin >> s;
    for(char c: s){
        freqs.insert(c);
    }
    
    cout << (freqs.size() % 2 == 0 ? "CHAT WITH HER!" : "IGNORE HIM!") << endl;
 

    return 0;
}
