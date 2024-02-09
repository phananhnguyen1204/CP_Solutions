
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

int n;

int main()
{
    cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; i++){
        cin >> v[i];
    }
    int res = 0;
    int cnt = 0;
    int min_value = 1e9;
    for(int i = 0; i < n; i++){
        if(min_value > v[i]){
            min_value = v[i];
            res = i;
            cnt = 1;
        }
        else if(min_value == v[i]){
            cnt++;
        }
    }
    if(cnt != 1){
        cout << "Still Rozdil" << endl;
    }
    else{
        cout << (res+1) << endl;
    }
    

    return 0;
}
