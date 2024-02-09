
#include <bits/stdc++.h>
#define MAX 1e9 + 5
using namespace std;


string s;


int main()
{
    cin >> s;
    int cnt_odd = 0;
    vector<int> freqs(26,0);
    for(auto c: s){
        freqs[c - 'a']++;
        if(freqs[c - 'a'] %2 == 1){
            cnt_odd++;
        }
        else{
            cnt_odd--;
        }
    }
    if(cnt_odd <= 1 || cnt_odd % 2 == 1){
        cout << "First" << endl;
    }
    else{
        cout << "Second";
    }


    

    return 0;
}
