
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

string s, t;

int main()
{
    cin >> s >> t;
    if(s.length() != t.length()){
        cout << "NO";
        return 0;
    }
    int i = 0, j = t.length()-1;
    for(int i = 0; i < s.length(); i++){
        if(s[i] != t[j]){
            cout << "NO";
            return 0;
        }
        j--;
    }
    cout << "YES" << endl;


    return 0;
}
