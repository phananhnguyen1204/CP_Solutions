#include <bits/stdc++.h>

using namespace std;

int n,m,x;
queue<int> q;

int main()
{
    cin >> n >> m;
    for(int i =0 ; i < n; i++){
        cin >> x;
        q.push(x);
    }
    
    int cnt = 0;
    while(!q.empty()){
        int sum = 0;
        while(!q.empty() && q.front() + sum <= m){
            sum += q.front();
            q.pop();
        }
        cnt++;
    }
    
    cout << cnt;

    return 0;
}
