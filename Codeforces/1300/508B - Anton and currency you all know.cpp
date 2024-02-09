#include <iostream>

using namespace std;

string s;

int main()
{
    cin >> s;
    int n = s.length();
    bool found = false;
    for(char c : s){
        if(c % 2 == 0){
            found = true;
        }
    }
    if(!found){
        cout << -1;
        return 0;
    }
    int r = s[n-1]  - '0';
    for(int i = 0; i < n; i++){
        int l = s[i] - '0';
        if(l % 2 == 0){
            if(l < r){
                swap(s[i],s[n-1]);
                cout << s;
                return 0;
            }
        }
    }
    for(int i = n-1; i >= 0; i--){
        int l = s[i] - '0';
        if(l % 2 == 0){
            if(l > r){
                swap(s[i],s[n-1]);
                cout << s;
                return 0;
            }
        }
    }

    return 0;
}
