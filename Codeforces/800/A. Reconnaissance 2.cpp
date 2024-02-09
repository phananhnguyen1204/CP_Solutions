
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
    int ind2 = 0, ind1 = n-1;
    int diff = abs(v[ind1] - v[ind2]);
    if(diff == 0){
        cout << ind1 + 1 << " " << ind2 + 1;
        return 0;
    }
    for(int i = 1; i < n; i++){
        if(diff > abs(v[i-1]-v[i])){
            ind2 = i;
            ind1 = i-1;
            diff = abs(v[i-1] - v[i]);
        }
    }
    cout << ind1 + 1 << " " << ind2 + 1 << endl;
    

    return 0;
}
