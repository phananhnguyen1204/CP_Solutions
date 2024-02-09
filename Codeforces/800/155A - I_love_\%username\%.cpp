#include <bits/stdc++.h>

using namespace std;


int n;



int main()
{
    cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; i++){
        cin >> v[i];
    }
    int min_res = v[0];
    int max_res = v[0];
    int cnt = 0;
    for(int i = 1; i < n; i++){
        if(v[i] > max_res){
            cnt++;
            max_res = v[i];
        }
        else if(v[i] < min_res){
            min_res = v[i];
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}
