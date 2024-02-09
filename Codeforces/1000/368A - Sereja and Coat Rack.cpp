#include <bits/stdc++.h>

using namespace std;

int n, d,x,m;
priority_queue<int,vector<int>,greater<int>> min_heap;


int main()
{
    cin >> n >> d;
    for(int i = 0; i < n; i++){
        cin >> x;
        min_heap.push(x);
    }
    cin >> m;
    int cnt = 0;
    for(int i = 0; i < m; i++){
        if(!min_heap.empty()){
            cnt += min_heap.top();
            min_heap.pop();
        }
        else{
            cnt -= d;
        }
    }
    cout << cnt;
    
    return 0;
}
