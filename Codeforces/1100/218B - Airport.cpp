
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

int n, m;


int main()
{
    cin >> n >> m;
    vector<int>v(m);
    int max_res = 0;
    int min_res = 0;
    priority_queue<int> max_heap;
    priority_queue<int,vector<int>,greater<int>> min_heap;
    for(int i = 0; i < m; i++){
        cin >> v[i];
        min_heap.push(v[i]);
        max_heap.push(v[i]);
    }
    for(int i = 0; i < n; i++){
        int top1 = max_heap.top();
        max_heap.pop();
        int top2 = min_heap.top();
        min_heap.pop();
        min_res += top2;
        max_res += top1;
        top2--;
        top1--;
        if(top1 > 0){
            max_heap.push(top1);
        }
        if(top2 > 0){
            min_heap.push(top2);
        }
    }
    cout << max_res << " " << min_res << endl;

    return 0;
}
