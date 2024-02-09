
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

string s, t;


int main()
{
    cin >> s;
    t = "hello";
    int i = 0;
    for(char c: s){
        if(c == t[i]){
            i++;
            if(i == t.length()){
                break;
            }
        }
    }
    if(i == t.length()){
        cout << "YES";
    }
    else{
        cout << "NO";
    }

    return 0;
}
