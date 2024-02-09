
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

int n,m,value;
queue<vector<int>> q;

int main()
{
    cin >> n >> m;
    int res = 0;
    for(int i = 0; i < n; i++){
        cin >> value;
        q.push({value,0,i});
    }
    while(!q.empty()){
        auto top = q.front();
        res = top[2];
        q.pop();
        if(top[0] > m + top[1]){
            q.push({top[0],top[1] + m,top[2]});
        }
    }
    cout << (res + 1);

    return 0;
}
