
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

int n,m;


int main()
{
    cin >> n >> m;
    vector<int> puzzles(m);
    for(int i = 0; i < m; i++){
        cin >> puzzles[i];
    }
    sort(puzzles.begin(), puzzles.end());
    int dif = INT_MAX;
    for(int i = (n-1); i <m;i++){
        dif = min(dif,(puzzles[i] - puzzles[i - n + 1]));
    }
    cout << dif;
    

    return 0;
}
