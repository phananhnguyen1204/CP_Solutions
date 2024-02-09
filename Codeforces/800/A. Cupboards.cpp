
#include <bits/stdc++.h>

using namespace std;

int n,l,r;

int main()
{
    cin >> n;
    int cntl = 0;
    int cntr = 0;
    for(int i = 0; i < n; i++){
        cin >> l >> r;
        if(l == 0){
            cntl++;
        }
        if(r == 0){
            cntr++;
        }
        
    }
    cout << (min(n - cntl,cntl) + min(n-cntr,cntr)) << endl;
 

    return 0;
}
