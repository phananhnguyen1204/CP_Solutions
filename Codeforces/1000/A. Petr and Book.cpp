
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

int n;

int main()
{
    cin >> n;
    vector<int> v(7);
    for(int i = 0; i < 7; i++){
        cin >> v[i];
    }
    
    int sum = 0;
    int i = 0;
    int res = 0;
    while(sum < n){
        sum += v[i];
        res = i;
        i = (i+1) % 7;
    }
    cout << (res+1) << endl;
    

    return 0;
}
