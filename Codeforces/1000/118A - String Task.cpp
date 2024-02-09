
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

string s;


int main()
{
    cin >> s;
    string res;
    for(char c: s){
        char curr = tolower(c);
        if(curr == 'a' || curr == 'e' || curr == 'o' || curr == 'u' || curr == 'i' || curr =='y'){
            continue;
        }
        else{
            res += ".";
            res += curr;
        }
    }
    cout << res;

    return 0;
}
