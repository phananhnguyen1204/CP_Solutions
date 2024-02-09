#include <bits/stdc++.h>

using namespace std;

int n,x;

int main()
{
    cin >> n;
    vector<int> v(n);
    int Limark;
    priority_queue<int> max_heap;
    for(int i =0 ; i < n; i++){
        cin >> x;
        if(i == 0){
            Limark = x;
        }
        else{
           max_heap.push(x);
        }
    }
    int cnt = 0;
    while(!max_heap.empty()&&Limark <= max_heap.top()){
        auto top = max_heap.top();
        max_heap.pop();
        top--;
        Limark++;
        if(top > 0){
            max_heap.push(top);
        }
        cnt++;
    }
    cout << cnt;
    return 0;
}
