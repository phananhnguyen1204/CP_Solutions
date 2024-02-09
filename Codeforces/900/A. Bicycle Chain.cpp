
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

int n,m;


int main()
{
    cin >> n;
    vector<int> pedal(n);
    for(int i = 0; i < n; i++){
        cin >> pedal[i];
    }
    cin >> m;
    vector<int> wheel(m);
    for(int i = 0; i < m; i++){
        cin >> wheel[i];
    }
    int max_res = -1e9;
    int cnt = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(wheel[j] % pedal[i] == 0){
                int frac = wheel[j] / pedal[i];
                if(frac > max_res){
                    max_res = frac;
                    cnt = 1;
                }
                else if(frac == max_res){
                    cnt++;
                }
            }
        }
    }
    cout << cnt;

    return 0;
}
